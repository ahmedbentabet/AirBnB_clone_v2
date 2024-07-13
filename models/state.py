#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
import os

STORAGE = os.getenv("HBNB_TYPE_STORAGE")


class State(BaseModel, Base):
    """ State class """

    __tablename__ = "states"

    if STORAGE == "db":
        name = Column(String(128), nullable=False)

        cities = relationship("City", backref="state", cascade="all, delete" )
    else:
        name = ""

        @property
        def cities(self):
            """Getter for cities when using FileStorage"""
            from models import storage

            # Get all City objects from storage
            all_cities = storage.all(City)
            city_list = []
            for city in all_cities.values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
