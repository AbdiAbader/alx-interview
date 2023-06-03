#!/usr/bin/python3
""" Prime Games"""
def generatePrimes(n):
    """Generates primes"""
    primes = []
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False

    for i in range(2, n + 1):
        if is_prime[i]:
            primes.append(i)

    return primes


def simulateGame(n):
    """ Simulate function """
    primes = generatePrimes(n)
    num_primes = len(primes)
    if num_primes % 2 == 0:
        return 'Ben'
    else:
        return 'Maria'


def isWinner(x, nums):
    """Check winners"""
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = simulateGame(n)
        if winner == 'Maria':
            maria_wins += 1
        elif winner == 'Ben':
            ben_wins += 1

    if maria_wins > ben_wins:
        return 'Maria'
    elif ben_wins > maria_wins:
        return 'Ben'
    else:
        return None
