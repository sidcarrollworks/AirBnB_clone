#!/usr/bin/python3
"""
sity class inherits from base class
"""
from models.base_model import BaseModel
import models


class City(BaseModel):
    """ city class inherits from base class """
    state_id = ""
    name = ""
