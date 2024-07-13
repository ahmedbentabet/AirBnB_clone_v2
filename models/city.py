#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import os

STORAGE = os.getenv("HBNB_TYPE_STORAGE")


class City(BaseModel, Base):
    """This class defines a city by various attributes"""
    __tablename__ = "cities"

    if STORAGE == "db":
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)

        # Relationship with Place objects
        places = relationship('Place', cascade='all, delete-orphan', backref='cities')

    else:
        state_id = ""
        name = ""
