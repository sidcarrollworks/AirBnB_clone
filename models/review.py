#!/usr/bin/python3
"""
review class inherits from base class
"""
from models.base_model import BaseModel
import models


class Review(BaseModel):
    """ review class inherits from base class """
    place_id = ""
    user_id = ""
    text = ""
