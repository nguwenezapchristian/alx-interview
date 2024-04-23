#!/usr/bin/python3
"""
A Program which generate Pascal's Triangle when given
the number of rows. It returns a list of lists of integers
representing the Pascal's triangle of n(rows)
"""


def pascal_triangle(n):
    triangle_list = []
    if n <= 0:
        return triangle_list
    i = 0
    while i < n:
        row = []
        j = 0
        while j <= i:
            if i == 0 or j == 0:
                num = 1
            else:
                """ Here i used // to get integer instead of a float
                    and this formula num = (num * (i - j + 1)) // j is
                    used to generate the exact value on each row and column
                """
                num = (num * (i - j + 1)) // j
            row.append(num)
            j += 1
        triangle_list.append(row)
        i += 1
    return triangle_list
