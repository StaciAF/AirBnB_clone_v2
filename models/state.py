#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all,delete,delete-orphan",
                          backref="state")

    @property
    def cities(self):
        '''
        Returns a list of City objects from storage linked to State
        '''
        city_list = []
        for key, val in models.storage.all().items():
            if val.state_id == self.id:
                city_list.append(val)
        return city_list
