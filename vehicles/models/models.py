
from sqlalchemy.schema import UniqueConstraint
from sqlalchemy import Table, Column, Integer, String, VARCHAR, LargeBinary, UnicodeText


class Location(db.Model):

    __tablename__ = "locations"

    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(128), nullable=False, unique=True) # Round Rock, North Austin,etc

    def __init__(self, location):
            self.location = location


class AvailableService(db.Model):

    __tablename__ = "available_services"

    # """ vehicle type and service type are composite primary key """
    id = db.Column(db.Integer, primary_key=True)
    vehicle_type_id = db.Column(db.Integer, db.ForeignKey('VehicleType.id'))  # foreign key to vehicle type
    service_type_id = db.Column(db.Integer, db.ForeignKey('ServiceType.id'))  # foreign key to service type
    vehicle_condition_id = db.Column(db.Integer, db.ForeignKey('VehicleCondition.id'))

    # $20 for mini on a car, $40 for full interior on truck, etc
    base_price = db.Column(db.Float, nullable=True)

    __table_args__ = (
        UniqueConstraint("vehicle_type_id", "service_type_id", "vehicle_condition_id", name="uk_available_services"),
    )

    def __init__(self, vehicle_type_id, service_type_id, vehicle_condition_id, base_price):
        self.vehicle_type_id = vehicle_type_id
        self.service_type_id = service_type_id
        self.vehicle_condition_id = vehicle_condition_id
        self.base_price = base_price


class ServiceType(db.Model):

    __tablename__ = "service_types"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False, unique=True) # computer friendly: mini, full_interior, full_detail, full_detail_w_compound
    display_name = db.Column(db.String(128), nullable=False) # Mini, Full Interior, etc
    description = db.Column(db.Text(), nullable=False) # example for mini: "Wash with vacuum, windows inside and out, tire shine, ..."
    available_services_ref = db.relationship('AvailableService', backref='ServiceType', lazy='joined')

    def __init__(self, name, display_name, description):
        self.name = name
        self.display_name = display_name
        self.description = description


class SpecialService(db.Model):

    __tablename__ = "special_services"

    id = db.Column(db.Integer, primary_key=True)
    vehicle_type_id = db.Column(db.Integer, db.ForeignKey('VehicleType.id'))  # foreign key to vehicle type
    # $20 for mini on a car, $40 for full interior on truck, etc
    name = db.Column(db.String(128), nullable=False)
    question = db.Column(db.String(128), nullable=False)
    price = db.Column(db.Float, nullable=False)

    __table_args__ = (
        UniqueConstraint("vehicle_type_id", "name", name="uk_special_services"),
    )

    def __init__(self, vehicle_type_id, name, question, price):
        self.vehicle_type_id = vehicle_type_id
        self.name = name
        self.question = question
        self.price = price


class VehicleCondition(db.Model):

    __tablename__ = "vehicle_condition"

    id = db.Column(db.Integer, primary_key=True)
    condition = db.Column(db.String(128), nullable=False, unique=True) # excellent, good, fair, dirty, etc...

    def __init__(self, condition):
        self.condition = condition


class VehicleType(db.Model):

    __tablename__ = "VehicleType"

    id = db.Column(db.Integer, primary_key=True)
    # car, crossover, truck, suv, etc
    type = db.Column(db.String(128), nullable=False, unique=True)
    # Car, Crossover (small SUV), Truck, SUV, etc
    display_text = db.Column(db.String(128), nullable=False)
    available_servicesref = db.relationship('AvailableService', backref = 'VehicleType', lazy = 'joined')

    def __init__(self, type, display_text):
        self.type = type
        self.display_text = display_text


class ZipCode(db.Model):

    __tablename__ = "zip_code"

    id = db.Column(db.Integer, primary_key=True)
    zip_code = db.Column(db.String(128), nullable=False, unique=True)
    price_increase = db.Column(db.Integer, nullable=True) # a percentage increase to the price. integer field should be fine here

    def __init__(self,zip_code,price_increase):
        self.zip_code = zip_code
        self.price_increase = price_increase
