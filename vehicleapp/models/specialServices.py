from __init__ import db
from __init__ import UniqueConstraint

class SpecialServices(db.Model):

    __tablename__ = "SpecialServices"
    
    id = db.Column(db.Integer, primary_key=True)
    vehicle_type_id = db.Column(db.Integer, db.ForeignKey(
        'VehicleType.id'))  # foreign key to vehicle type
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
