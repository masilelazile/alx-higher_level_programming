#!/usr/bin/python3
from sys import stderr

def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except (TypeError) as error:
        print("Exception: {}".format(error), file=stderr)
    except (ValueError) as error:
        print("Exception: {}".format(error), file=stderr)
        return False
    return True
