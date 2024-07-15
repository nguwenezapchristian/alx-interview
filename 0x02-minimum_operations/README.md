# Minimum Operations

## Overview

This project focuses on calculating the minimum number of operations required to achieve exactly `n` 'H' characters in a text file, starting with a single 'H'. The only operations allowed are "Copy All" and "Paste".

## Requirements

- Python 3.4.3
- Ubuntu 20.04 LTS

## Project Structure

- `0-minoperations.py`: Contains the implementation of the `minOperations` function.
- `0-main.py`: A script to test the `minOperations` function.
- `README.md`: This file, which provides an overview of the project.

## Function Prototype

```python
def minOperations(n)
```

### Parameters

- `n` (int): The target number of 'H' characters.

### Returns

- The minimum number of operations needed to achieve `n` 'H' characters.
- If `n` is impossible to achieve, return `0`.

## Example

```python
n = 4
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
# Output: Min number of operations to reach 4 characters: 4

n = 12
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
# Output: Min number of operations to reach 12 characters: 7

n = 9
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
# Output: Min number of operations to reach 9 characters: 6
```

## Implementation Details

### Prime Factorization

The solution uses prime factorization to determine the minimum number of operations. For each prime factor of `n`, the number of operations is the sum of the prime factors, representing the series of "Paste" operations following a "Copy All".

### Edge Cases

- If `n <= 1`, the function returns `0` as it's not possible to achieve `n` characters using the given operations.

## Usage

To run the tests and see the results, use:

```bash
./0-main.py
```

Ensure you have execute permissions for the script:

```bash
chmod +x 0-main.py
```

## Author

[Nguweneza P Christian]