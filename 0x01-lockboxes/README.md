# Lockboxes

## Overview

This project aims to implement a method to determine if all boxes in a list of locked boxes can be opened, starting from the first box. Each box may contain keys to other boxes, and the goal is to determine if all boxes can be unlocked by using the keys contained within them.

## Functionality

The `canUnlockAll` function takes a list of lists representing the locked boxes, where each inner list contains the indices of keys it holds. It returns `True` if all boxes can be opened, starting from the first box, or `False` otherwise.

## Usage

To use the `canUnlockAll` function, follow these steps:

1. Import the function into your Python script:
    ```python
    from lockboxes import canUnlockAll
    ```

2. Call the function with a list of locked boxes as the argument:
    ```python
    boxes = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes))  # Output: True
    ```

3. Ensure that your locked boxes list follows the required format:
   - Each inner list represents a box.
   - The inner lists contain the indices of keys it holds.

## Requirements

- Allowed editors: vi, vim, emacs
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3.4.3
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- A README.md file, at the root of the folder of the project, is mandatory
- Code should be documented
- Code should use the PEP 8 style (version 1.7.x)
- All files must be executable

## Implementation Details

The solution uses a breadth-first search (BFS) approach to traverse through the boxes and keys, ensuring efficient exploration and checking if all boxes can be unlocked. It includes necessary checks and data structures to handle edge cases and maintain the state of the traversal accurately.

## Authors

- [Nguweneza P Christian](https://github.com/nguwenezapchristian/alx-interview)