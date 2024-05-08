#!/usr/bin/python3
"""
a method that determines if all the boxes can be opened
"""


def canUnlockAll(boxes):
    """
    Determine if all boxes can be unlocked starting from the first box.

    Args:
    - boxes: A list of lists where each inner list represents a box and
    contains the indices of keys it holds.

    Returns:
    - True if all boxes can be opened, else return False.
    """

    # if not boxes:
    #     return False

    num_boxes = len(boxes)
    visited = set()
    keys_to_visit = [0]

    while keys_to_visit:
        current_box = keys_to_visit.pop(0)
        if current_box in visited:
            continue
        visited.add(current_box)
        keys_to_visit.extend(boxes[current_box])

    return len(visited) == num_boxes
