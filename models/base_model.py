#!/usr/bin/env python3
"""defines the class BaseModel"""
from datetime import datetime
import uuid


class BaseModel:
    """defines all common attributes/methods for other classes"""
    def __init__(self):
        """initialize the instance attributes"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """return the string representation of an object"""
        return "{} {} {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """update the updated_at atrr with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__"""
        pass



if __name__ == "__main__":
    uthman = BaseModel()
    print(uthman.created_at)
    print(uthman)
