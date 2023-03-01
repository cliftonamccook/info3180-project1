from . import db


class Property(db.Model):
    __tablename__ = "properties"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256))
    bedrooms = db.Column(db.String(3))
    bathrooms = db.Column(db.String(3))
    location = db.Column(db.String(256))
    price = db.Column(db.String(15))
    type = db.Column(db.String(10))
    description = db.Column(db.Text())
    photo_filename = db.Column(db.String(256))


    def __init__(self, title, _type, location, price, description, bedrooms, bathrooms, photo_filename):
        self.title = title
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.location = location
        self.price = price
        self.type = _type
        self.description = description
        self.photo_filename = photo_filename


    def __repr__(self):
        return '<Property %r>' % (self.title)