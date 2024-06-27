#!/usr/bin/python3
""" Island Perimeter """


def island_perimeter(grid):
    """
    Calculate the perimeter of an island represented by 1s in a grid of 0s and 1s.

    Args:
        grid (list of list of int): 2D list representing the grid.

    Returns:
        int: Perimeter of the island.
    """
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                """ Check the four neighboring cells """
                if i == 0 or grid[i-1][j] == 0:
                    """ Check top """
                    perimeter += 1
                if i == rows - 1 or grid[i+1][j] == 0:
                    """ Check bottom """
                    perimeter += 1
                if j == 0 or grid[i][j-1] == 0:
                    """ Check left """
                    perimeter += 1
                if j == cols - 1 or grid[i][j+1] == 0:
                    """ Check right """
                    perimeter += 1

    return perimeter
