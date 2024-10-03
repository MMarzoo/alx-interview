#!/usr/bin/python3
"""
prime_game
"""


def isWinner(x, nums):
    """
    Determines the winner in the prime game using
    Eratosthenes prime sieving algorithm
    """
    if x <= 0 or nums is None:
        return None

    maria_wins = 0
    ben_wins = 0

    prime_game = [1 for x in range(sorted(nums)[-1] + 1)]

    prime_game[0] = 0
    prime_game[1] = 0

    for num in range(2, len(prime_game)):
        for i in range(2, len(prime_game)):
            try:
                prime_game[i * num] = 0
            except IndexError:
                break

    for n in nums:
        if sum(prime_game[0:n + 1]) % 2 == 0:
            ben_wins += 1

        else:
            maria_wins += 1

    if ben_wins > maria_wins:
        return "Ben"
    if ben_wins < maria_wins:
        return "Maria"
    return None
