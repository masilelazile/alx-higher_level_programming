#!/usr/bin/python3
"""
Una función que retona la representación JSON de un objeto(string)
"""


import json


def to_json_string(my_obj):
    """
    Retorna la representación JSON de un objeto
    """
    return json.dumps(my_obj)
