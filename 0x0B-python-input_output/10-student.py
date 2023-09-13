#!/usr/bin/python3
"""Escriba una clase Estudiante que defina a un estudiante"""


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
        """Recupera una representación de diccionario de
        una instancia de Estudiante"""
        if attrs is None:
            return self.__dict__
        d = {}
        for i in attrs:
            try:
                d[i] = self.__dict__[i]
            except KeyError:
                pass
        return d
