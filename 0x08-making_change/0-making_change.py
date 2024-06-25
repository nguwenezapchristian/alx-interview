#!/usr/bin/python3
def makeChange(coins, total):
    """Create a list to store the minimum number
    of coins needed for each amount up to the total.
    Return the minimum number of coins needed for each
    amount up to the total, or -1 if it is not possible
    to make change for each amount up to the total
    """
    dp = [float('inf')] * (total + 1)

    """Base case: 0 coins are needed to make 0 total"""
    dp[0] = 0

    """Iterate over each coin value"""
    for coin in coins:
        """Iterate over each amount up to the total"""
        for amount in range(coin, total + 1):
            """Update the minimum number of coins needed
            for the current amount
            """
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    """If the minimum number of coins needed for the total is still infinity,
    return -1
    """
    if dp[total] == float('inf'):
        return -1
    """Otherwise, return the minimum number of coins needed for the total"""
    return dp[total]
