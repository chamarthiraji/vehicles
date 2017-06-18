from __init__ import db
from __init__ import UniqueConstraint
from __init__ import UnicodeText
from __init__ import VARCHAR
from __init__ import LargeBinary

class AvailableServices(db.Model):

    __tablename__ = "AvailableServices"
    
    # """ vehicle type and service type are composite primary key """
    id = db.Column(db.Integer, primary_key=True)
    vehicle_type_id = db.Column(db.Integer, db.ForeignKey(
        'VehicleType.id'))  # foreign key to vehicle type
    service_type_id = db.Column(db.Integer, db.ForeignKey(
        'ServiceType.id'))  # foreign key to service type
    vehicle_condition_id = db.Column(db.Integer,
        db.ForeignKey('VehicleCondition.id'))

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
