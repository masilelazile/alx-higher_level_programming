#!/usr/bin/python3
"""
Una funcion que agrega un string al final de un archivo utf-8
y retorne el número de caracteres escritos
"""


def append_write(filename="", text=""):
    """
    Escribir un string en un archivo utf-8
    """
    with open(filename, 'a') as f:
        f.write(text)
    return len(text)
