#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.place import place_amenity
import os

STORAGE = os.getenv("HBNB_TYPE_STORAGE")


class Amenity(BaseModel, Base):
    """Represents an amenity for a place"""

    __tablename__ = 'amenities'

    if STORAGE == "db":
        name = Column(String(128), nullable=False)
        # Many-to-Many relationship with Place
        # place_amenities = relationship(
        #     "Place", secondary=place_amenity,
        #     backref="amenities", viewonly=False
        # )
    else:
        name = ""
