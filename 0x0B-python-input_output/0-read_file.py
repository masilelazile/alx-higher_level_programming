#!/usr/bin/python3
"""
Lee un archivo y lo imprime en la salida estándar
"""


def read_file(filename=""):
    """
    Lee un archivo y lo imprime en la salida estándar
    """
    with open(filename, 'r') as f:
        print(f.read(), end="")
