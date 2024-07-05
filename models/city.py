#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.place import Place  # Import Place to establish relationship


class City(BaseModel, Base):
    """This class defines a city by various attributes"""
    __tablename__ = "cities"

    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)

    # Relationship with Place objects
    places = relationship('Place', cascade='all, delete-orphan', backref='cities')
