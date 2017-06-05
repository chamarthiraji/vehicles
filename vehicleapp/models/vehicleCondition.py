from __init__ import db
from __init__ import UniqueConstraint

class VehicleCondition(db.Model):

	__tablename__ = "VehicleCondition"
	
	id = db.Column(db.Integer, primary_key=True)
	condition = db.Column(db.String(128), nullable=False) # excellent, good, fair, dirty, etc...

	__table_args__ = (
		UniqueConstraint("condition", name="uk_vehicleCondition"),
	)
	
def __init__(self, condition):
        self.condition = condition
        

