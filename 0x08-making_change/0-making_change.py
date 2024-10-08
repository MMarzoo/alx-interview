#!/usr/bin/python3
"""
Making Change module
"""


def makeChange(coins, total):
    """
    Function to calculate the minimum number of coins needed to make change
    for a given amount.
    """
    if not coins or coins is None:
        return -1
    if total <= 0:
        return 0
    change = 0
    coins = sorted(coins)[::-1]
    for coin in coins:
        while coin <= total:
            total -= coin
            change += 1
        if (total == 0):
            return change
    return -1
