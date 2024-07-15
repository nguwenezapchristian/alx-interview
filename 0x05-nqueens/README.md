# N Queens

## Overview

The N Queens problem is a classic computer science and mathematics problem that involves placing N non-attacking queens on an N×N chessboard. This project implements a solution using the backtracking algorithm in Python.

## Requirements

- Python 3.4.3
- Ubuntu 20.04 LTS

## Project Structure

- `0-nqueens.py`: The main script to solve the N Queens problem.
- `README.md`: This file, providing an overview of the project.

## Usage

The script should be executed from the command line with the following syntax:

```bash
./0-nqueens.py N
```

Where `N` is the size of the chessboard and the number of queens. `N` must be an integer greater than or equal to 4.

### Examples

```bash
$ ./0-nqueens.py 4
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]

$ ./0-nqueens.py 6
[[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]]
[[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]]
[[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]]
[[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1]]
```

### Error Handling

- If the wrong number of arguments is provided:

```bash
$ ./0-nqueens.py
Usage: nqueens N
```

- If `N` is not an integer:

```bash
$ ./0-nqueens.py not_a_number
N must be a number
```

- If `N` is less than 4:

```bash
$ ./0-nqueens.py 3
N must be at least 4
```

## Author

[Nguweneza P Christian]