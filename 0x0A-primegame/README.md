# Prime Game

## Overview

This project involves creating an algorithm to determine the winner of a game played between two players, Maria and Ben. The game is played over multiple rounds, where each round involves a set of consecutive integers starting from 1 up to and including `n`. The players take turns picking prime numbers and removing them and their multiples from the set. The player who cannot make a move loses the game.

## Requirements

- Python 3.4.3
- Ubuntu 20.04 LTS

## Project Structure

- `0-prime_game.py`: Contains the implementation of the `isWinner` function.
- `main_0.py`: A script to test the `isWinner` function.
- `README.md`: This file, which provides an overview of the project.

## Function Prototype

```python
def isWinner(x, nums)
```

### Parameters

- `x` (int): The number of rounds.
- `nums` (list of int): An array of integers where each integer `n` represents the upper limit of the set for that round.

### Returns

- The name of the player who won the most rounds ("Maria" or "Ben").
- If the winner cannot be determined, return `None`.

## Example

```python
x = 3
nums = [4, 5, 1]

print("Winner: {}".format(isWinner(x, nums)))
```

Expected Output:
```
Winner: Ben
```

## Implementation Details

### Sieve of Eratosthenes

The `sieve` function generates all prime numbers up to the maximum value of `n` in `nums` using the Sieve of Eratosthenes algorithm.

### Game Simulation

The game simulation involves:
1. Counting the number of prime numbers and their multiples that can be removed for each value of `n`.
2. Determining the winner for each round based on the count of removable primes and their multiples.
3. Counting the total number of wins for Maria and Ben to determine the overall winner.

### Counting Prime Multiples

The `count_prime_multiples` function counts how many numbers up to `n` are multiples of prime numbers.

### Overall Winner Determination

After simulating all rounds, the number of wins for Maria and Ben are compared to determine the overall winner.

## Usage

To run the tests and see the result, use:

```bash
./main_0.py
```

Ensure you have execute permissions for the script:

```bash
chmod +x main_0.py
```

## Author

[Nguweneza P Christian]