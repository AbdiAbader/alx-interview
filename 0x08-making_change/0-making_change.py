#!/usr/bin/python3
""" Make a real change of coins"""


def makeChange(coins, total):
    """makeChange function"""
    if total <= 0:
        return 0
    if coins is None or len(coins) == 0:
        return -1

    coins.sort(reverse=True)
    numCoins = 0

    for coin in coins:
        while total >= coin:
            total -= coin
            numCoins += 1

    if total != 0:
        return -1

    return numCoins
