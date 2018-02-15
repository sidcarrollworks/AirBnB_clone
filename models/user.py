#!/usr/bin/python3
"""
class User that inherits from BaseModel
"""
from models.base_model import BaseModel
import models


class User(BaseModel):
    """
    User class inherits from BaseModel
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
