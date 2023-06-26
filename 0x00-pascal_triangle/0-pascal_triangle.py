#!/usr/bin/python3
"""
python code for pascal_triangle
"""


def pascal_triangle(n):
    """ padcal triabgle that returns a list of lists of integers
    representing the Pascal’s triangle of n:
    """

    tri = []
    if n > 0:
        for i in range(1, n + 1):
            arr = []
            C = 1
            for j in range(1, i + 1):
                arr.append(C)
                C = C * (i - j) // j
            tri.append(arr)
    return tri
