#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey, Float, Table
from sqlalchemy.orm import relationship
from os import getenv


place_amenity = Table('place_amenity', Base.metadata, Column('place_id',
        String(60), ForeignKey('places.id'), nullable=False, primary_key=True),
        Column('amenity_id', String(60), ForeignKey('amenities.id'), nullable=False, primary_key=True))


class Place(BaseModel, Base):
    """ defines class Place with multiple attributes """
    __tablename__ = 'places'
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        review = relationship('Review', cascade='all, delete, delete-orphan', backref='place')
        amenities = relationship('Amenity', secondary=place_amenity, viewonly=False)
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=False)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    else:
        @property
        def reviews(self):
            """ returns a list of Review objects with place_id matching Place.id """
            from models import storage
            return self.reviews
        @property
        def amenities(self):
            """ returns a list of Amenity objects with amenity_id matching Amenity.id """
            from models import storage
            return self.amenities
