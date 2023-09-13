#!/usr/bin/python3
"""returns a list of lists of integers representing
the Pascals triangle of n"""


def pascal_triangle(n):
    """FUntion pascal triangle """
    pascal_list = []
    for _ in range(n):
        row = [1]
        if pascal_list:
            last_row = pascal_list[-1]
            row.extend([sum(pair) for pair in zip(last_row, last_row[1:])])
            row.append(1)
        pascal_list.append(row)
    return

def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


print_triangle(pascal_triangle(5))
