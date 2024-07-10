#!/usr/bin/python3
""" Place Module for HBNB project """
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from models.review import Review


# Join table to link Place and Amenity
place_amenity = Table(
                'place_amenity',
                Base.metadata,
                Column('place_id', String(60), ForeignKey('places.id'),
                    primary_key=True, nullable=False),
                Column('amenity_id', String(60), ForeignKey('amenities.id'),
                   primary_key=True, nullable=False)
)

class Place(BaseModel, Base):
    """ A place to stay """

    __tablename__ = 'places'

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)

    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []

    # Relationship with Review for DBStorage
    reviews = relationship('Review', backref='place', cascade='all, delete-orphan')
    # Relationship with Amenity using the join table place_amenity
    amenities = relationship("Amenity", secondary=place_amenity, 
                            back_populates="place_amenities", viewonly=False)

    @property
    def reviews(self):
        """Getter for reviews when using FileStorage"""
        from models import storage, storage_type

        if storage_type == 'db':
            return self.reviews
        else:
            all_reviews = storage.all(Review)
            review_list = []
            for review in all_reviews.values():
                if review.place_id == self.id:
                    review_list.append(review)
            return review_list

    @property
    def amenities(self):
        """
        Getter attribute amenities that returns
        the list of Amenity instances
        """
        from models import storage, storage_type
        from models.amenity import Amenity
        if storage_type == 'db':
            return self.amenities
        else:
            amenity_list = []
            for amenity_id in self.amenity_ids:
                amenity = storage.get(Amenity, amenity_id)
                if amenity:
                    amenity_list.append(amenity)
            return amenity_list

    @amenities.setter
    def amenities(self, obj):
        """
        Setter attribute amenities that handles append method
        for adding an Amenity.id
        """
        from models.amenity import Amenity
        if isinstance(obj, Amenity):
            self.amenity_ids.append(obj.id)
