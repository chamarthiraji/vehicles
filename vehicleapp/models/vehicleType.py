from __init__ import db
from __init__ import UniqueConstraint

class VehicleType(db.Model):

	__tablename__ = "VehicleType"
	
	id = db.Column(db.Integer, primary_key=True)
	# car, crossover, truck, suv, etc
	type = db.Column(db.String(128), nullable=False)
	# Car, Crossover (small SUV), Truck, SUV, etc
	display_text = db.Column(db.String(128), nullable=False)
	available_servicesref = db.relationship('AvailableServices'
		, backref = 'VehicleType'
		, lazy = 'joined')   

	__table_args__ = (
		UniqueConstraint("type", name="uk_vehicleType"),
	)

	def __init__(self, type, display_text):
		self.type = type
		self.display_text = display_text
