#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City", cascade="all,delete,delete-orphan",
                              backref="state")

    else:
        @property
        def cities(self):
            '''
            Returns a list of city objects with a state_id matching state.id
            '''
            from models import storage
            return [y for x, y in storage.all(City).items()
                    if y.state_id == self.id]
