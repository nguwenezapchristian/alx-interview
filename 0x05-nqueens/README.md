# N Queens Problem

## Overview

The N Queens problem is a classic problem in computer science and mathematics, where the objective is to place N queens on an N×N chessboard so that no two queens can attack each other. This project solves the N Queens problem using a backtracking algorithm implemented in Python.

## Requirements

- **Language**: Python 3.4.3
- **OS**: Ubuntu 20.04 LTS
- **Coding Style**: PEP 8 (version 1.7.*)
- **File Requirements**:
  - All Python files must start with the shebang `#!/usr/bin/python3`
  - All files should end with a new line
  - Files should be executable

## Usage

The main script to run the program is `0-nqueens.py`.

### Command Line Arguments

- `nqueens N`: where `N` is the size of the chessboard (must be an integer greater than or equal to 4).

### Example

To run the program with a 4×4 chessboard:

```bash
./0-nqueens.py 4
```

### Output

The program will print all the possible solutions, one solution per line. Each solution is represented as a list of lists, where each inner list contains the row and column indices of a queen.

Example output for `N = 4`:

```plaintext
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]
```

## Implementation Details

### Backtracking Algorithm

The backtracking algorithm is used to explore all potential configurations of queens on the board. It places queens one by one in different columns and checks for conflicts. If a conflict is found, it backtracks and tries another position.

### Safety Check

The `is_safe` function checks whether a queen can be placed at a given position without being attacked by other queens. It checks the current row, upper diagonal, and lower diagonal on the left side.

### Main Function

The `solve_nqueens` function initializes the chessboard and starts the backtracking process. It collects all valid solutions and prints them.

## Running the Script

Make sure to set executable permissions for the script:

```bash
chmod +x 0-nqueens.py
```

Then, run the script with the desired board size:

```bash
./0-nqueens.py 6
```