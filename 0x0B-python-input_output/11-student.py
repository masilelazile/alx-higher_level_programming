#!/usr/bin/python3
"""11. Student to disk and reload"""


class Student:
    """ Student class """
    first_name = None
    last_name = None
    age = None

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Public method to JSON """
        if attrs is None:
            return self.__dict__
        d = {}
        for i in attrs:
            try:
                d[i] = self.__dict__[i]
            except KeyError:
                pass
        return d

    def reload_from_json(self, json):
        """Public method reload from json """
        if type(json) is dict:
            for i in json:
                setattr(self, i, json[i])
