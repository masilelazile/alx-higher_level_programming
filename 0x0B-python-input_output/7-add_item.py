#!/usr/bin/python3
"""
 un script que agrega todos los argumentos a una lista,
 y los guarda en un archivo
"""


import json
from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


try:
    python_objet = load_from_json_file('add_item.json')
except FileNotFoundError:
    python_objet = []
for x in range(1, len(argv)):
    python_objet.append(argv[x])
save_to_json_file(python_objet, 'add_item.json')
