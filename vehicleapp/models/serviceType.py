from __init__ import db
from __init__ import UniqueConstraint

class ServiceType(db.Model):

	__tablename__ = "ServiceType"
	
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(128), nullable=False) # computer friendly: mini, full_interior, full_detail, full_detail_w_compound
	display_name = db.Column(db.String(128), nullable=False) # Mini, Full Interior, etc
	description = db.Column(db.Text(), nullable=False) # example for mini: "Wash with vacuum, windows inside and out, tire shine, ..."
	available_servicesref = db.relationship('AvailableServices'
		, backref = 'ServiceType'
		, lazy = 'joined')   

	__table_args__ = (
		UniqueConstraint("name", name="uk_serviceType"),
	)

	def __init__(self, name, display_name, description):
		self.name = name
		self.display_name = display_name
		self.description = description
        

        
