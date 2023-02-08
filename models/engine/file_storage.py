#!/usr/bin/env python3
"""
A simple storage engine that serializes instances to a
JSON file and deserializes JSON file to instances.
"""
import json


class FileStorage:
    """
    `FileStorage` uses JSON to serialize and deserializes
    object instances, while also handling saving to an
    abstract storage file.
    + ``__file_path``: string - path to the JSON file (ex: file.json)
    + ``__objects``: dictionary - empty but will store all objects
      by ``<class name>.id``.
    """
    __file_path = "file.json"
    __objects = {}

    # Public instance methods
    def all(self):
        """Simply return the dictionary ``__objects``"""
        return self.__objects

    def new(self, obj):
        """Sets in ``__objects`` the ``obj`` with key
        ``<obj class name>.id``"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects.update({key: obj.to_dict()})

    def save(self):
        """Serializes ``__objects`` to the JSON file ``__file_path``."""
        with open(self.__file_path, "w", encoding="utf-8") as fi:
            if self.__objects is not None or self.__objects != {}:
                json.dump(self.__objects, fi)

    def reload(self):
        """Deserializes the JSON file to ``__objects`` only if
        ``__file_path`` exists, otherwise; do nothing and no
        exception should be raised."""
        try:
            with open(self.__file_path, "r", encoding="utf-8") as fi:
                self.__objects = json.loads(fi.read())
        except FileNotFoundError:
            pass
        except json.decoder.JSONDecodeError:
            pass
