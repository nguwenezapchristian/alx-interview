#!/usr/bin/python3
""" Making Change """


def makeChange(coins, total):
    """
    Determine the minimum number of coins needed to meet a given total amount,
    given a pile of coins with different denominations.

    Args:
        coins (list): List of the values of the coins in your possession.
        total (int): The total amount to be made up.

    Returns:
        int: Fewest number of coins needed to meet the total.
             If total is 0 or less, return 0.
             If the total cannot be met by any number of coins, return -1.
    """
    if total <= 0:
        return 0

    # Initialize the DP array with a size of (total + 1) and set all elements to a large value
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Iterate over each coin
    for coin in coins:
        # Update the DP array values for all amounts >= coin
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
