#!/usr/bin/python3
"""
Making Change
"""

def makeChange(coins, total):
    """Edge case: if total is 0 or less, return 0"""
    if total <= 0:
        return 0

    """Initialize the DP array"""
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    """Populate the DP array"""
    for coin in coins:
        for amount in range(coin, total + 1):
            """Update the DP array"""
            if dp[amount - coin] != float('inf'):
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    """If dp[total] is still infinity, return -1"""
    return dp[total] if dp[total] != float('inf') else -1
