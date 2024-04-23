#!/usr/bin/python3
"""
A Program which generate Pascal's Triangle when given
the number of rows. It returns a list of lists of integers
representing the Pascal's triangle of n(rows)
"""


def pascal_triangle(n):
    """ returns an empty list if n <= 0 """
    triangle_list = []
    if n <= 0:
        return triangle_list
    i = 0
    while i < n:
        row = [1] * (i + 1)
        j = 1
        while j < i:
            """ Here is used list comprehension in
            find the exact number for each position
            """
            row[j] = triangle_list[i - 1][j - 1] + triangle_list[i - 1][j]
            j += 1
        triangle_list.append(row)
        i += 1
    return (triangle_list)
