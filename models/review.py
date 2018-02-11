#!/usr/bin/python3
"""
review class inherits from base class
"""
from models.base_mode import BaseModel


class Amenity(BaseModel):
    """ review class inherits from base class """
    place_id = ""
    user_id = ""
    text = ""
