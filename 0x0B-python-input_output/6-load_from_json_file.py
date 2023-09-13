#!/usr/bin/python3
"""
 Una función que crea un objeto a partir de un archivo de json
"""


import json


def load_from_json_file(filename):
    """
    Crea un objeto a partir de un archivo de texto, usando un formato JSON
    """
    with open(filename, 'r') as f:
        objet_py = json.loads(f.read())
    return objet_py
