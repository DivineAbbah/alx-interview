#!/usr/bin/python3
"""changes comes module"""


def makeChange(coins, total):
    if total <= 0:
        return 0

    coins.sort(reverse=True)  # sort from highest to lowest value

    count = 0
    for coin in coins:
        while total >= coin:
            total -= coin
            count += 1

    if total > 0:
        return -1  # if total cannot be met by available coins

    return count  # fewest coins needed
