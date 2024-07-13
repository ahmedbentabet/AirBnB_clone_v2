#!/usr/bin/python3
"""This module defines a class User"""
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
import os

STORAGE = os.getenv("HBNB_TYPE_STORAGE")


class User(BaseModel, Base):
    """This class defines a user by various attributes"""

    __tablename__ = 'users'  # Table name in the database

    if STORAGE == "db":
        email = Column(String(128), nullable=False)  # not nullable
        password = Column(String(128), nullable=False)  # not nullable
        first_name = Column(String(128))  # nullable
        last_name = Column(String(128))  # nullable

        # Relationship with Place objects
        places = relationship('Place', cascade='all, delete-orphan', backref='user')

        # Relationship with Review
        reviews = relationship('Review', backref='user', cascade='all, delete-orphan')
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""
