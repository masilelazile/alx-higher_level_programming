#!/usr/bin/python3
"""
    una funcion que retorna un objeto representado por una cadena JSON
"""


import json


def from_json_string(my_str):
    """
    Retorna el objeto representado por una cadena JSON
    """
    return json.loads(my_str)
