from __init__ import db
from __init__ import UniqueConstraint

class ZipCode(db.Model):	

	__tablename__ = "ZipCode"
    
	id = db.Column(db.Integer, primary_key=True)
	zip_code = db.Column(db.String(128), nullable=False)
	price_increase = db.Column(db.Integer, nullable=True) # a percentage increase to the price. integer field should be fine here

	__table_args__ = (
		UniqueConstraint("zip_code", name="uk_zipcode"),
	)

def __init__(self,zip_code,price_increase):

        self.zip_code = zip_code
        self.price_increase = price_increase