#!/usr/bin/python3
"""
Una función que escriba un estring en un archivo utf-8
y retorne el número de caracteres escritos
"""


def write_file(filename="", text=""):
    """
    Escribir un string en un archivo utf-8
    """
    with open(filename, 'w') as f:
        f.write(text)
    return len(text)
