from __init__ import db
from __init__ import UniqueConstraint

class Location(db.Model):

	__tablename__ = "Location"

	id = db.Column(db.Integer, primary_key=True)
	location = db.Column(db.String(128), nullable=False) # Round Rock, North Austin,etc

	__table_args__ = (
		UniqueConstraint("location", name="uk_location"),
	)

def __init__(self, location):
        self.location = location