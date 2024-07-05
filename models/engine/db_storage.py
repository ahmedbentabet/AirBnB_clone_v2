#!/usr/bin/python3
"""This module defines a class to manage db storage for hbnb clone"""
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage():
    """ DBStorage class """
    __engine = None  # Holds the SQLAlchemy engine (connection manager)
    __session = None  # Holds the database session (workspace)

    def __init__(self):
        """Initializes the DBStorage engine"""

        USER = getenv('HBNB_MYSQL_USER')
        PWD = getenv('HBNB_MYSQL_PWD')
        HOST = getenv('HBNB_MYSQL_HOST')
        DB = getenv('HBNB_MYSQL_DB')
        ENV = getenv('HBNB_ENV')

        # Create the connection string using environment variables
        conn_str = f"mysql+mysqldb://{USER}:{PWD}@{HOST}/{DB}"

        # Create the SQLAlchemy engine (connection manager)
        self.__engine = create_engine(conn_str, pool_pre_ping=True)

        if ENV == 'test':
            # Drop all tables for testing
            Base.metadata.drop_all(self.__engine)
            print("All tables dropped because HBNB_ENV is set to 'test'.")

    def all(self, cls=None):
        """Queries the database for all objects of a given class"""
        objects = {}
        if cls is None:
            # Query all types of objects
            for model_class in [User, State, City, Amenity, Place, Review]:
                for obj in self.__session.query(model_class).all():
                    key = f"{model_class.__name__}.{obj.id}"
                    objects[key] = obj
        else:
            # Query only objects of the specified class
            for obj in self.__session.query(cls).all():
                key = f"{cls.__name__}.{obj.id}"
                objects[key] = obj
        return objects

    def new(self, obj):
            """Adds an object to the current database session"""
            self.__session.add(obj)

    def save(self):
            """Commits all changes of the current database session"""
            self.__session.commit()

    def delete(self, obj=None):
            """Deletes an object from the current database session"""
            if obj is not None:
                self.__session.delete(obj)

    def reload(self):
        """Creates all tables and a new session"""
        from models.base_model import Base
        from sqlalchemy.orm import sessionmaker, scoped_session
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        # Create all tables
        Base.metadata.create_all(self.__engine)

        # Create a session factory
        session_factory = sessionmaker(bind=self.__engine,
                                        expire_on_commit=False)

        # Create a thread-safe session using scoped_session
        self.__session = scoped_session(session_factory)
