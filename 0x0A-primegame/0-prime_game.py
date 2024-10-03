#!/usr/bin/python3
"""
Prime_Game
"""


def SieveOfEratosthenes(n):
    """Returns a list of prime numbers up to
    n using the Sieve of Eratosthenes."""
    primes = [True] * (n + 1)
    primes[0], primes[1] = False, False

    p = 2
    while (p * p <= n):
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1

    return [i for i in range(n + 1) if primes[i]]


def isWinner(x, nums):
    """Determines who wins the most rounds between Maria and Ben."""
    if not nums or x <= 0:
        return None

    max_n = max(nums)
    primes = SieveOfEratosthenes(max_n)
    prime_set = set(primes)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        primes_in_game = [p for p in primes if p <= n]
        if not primes_in_game:
            ben_wins += 1
            continue

        turn = 0

        while primes_in_game:
            current_prime = primes_in_game[0]
            primes_in_game = [p for p in primes_in_game
                              if p % current_prime != 0]
            turn ^= 1  # Switch turns

        if turn == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
