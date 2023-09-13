#!/usr/bin/python3
"""
 Una funcion que escribe un objeto en un archivo de texto,
 usando un formato JSON
"""


import json


def save_to_json_file(my_obj, filename):
    """
    Escribir un objeto en un archivo de texto, usando un formato JSON
    """
    with open(filename, 'w') as f:
        f.write(json.dumps(my_obj))
    return 0
