#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.__init__ import storage
from os import environ


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    if environ['HBNB_TYPE_STORAGE'] == 'db':
        cities = relationship("City", cascade="all,delete,delete-orphan",
                              backref="state")

    elif environ['HBNB_TYPE_STORAGE'] == 'file':
        def cities(self):
            return [{x: y} for x, y in storage._FileStorage__objects.items()
                    if 'City' in x and y.state_id == self.id]
