#!/usr/bin/python3
"""
    Module loopup function
"""


def lookup(obj):
    """ Retorna todos los atributos y métodos de un objeto

    Args:
        obj: una clase como objeto heredado

    Returns: dir de objeto, lista
    """
    return dir(obj)
