#!/usr/bin/python3
def isWinner(x, nums):
    if not nums or x < 1:
        return None

    def sieve(max_n):
        primes = [True] * (max_n + 1)
        primes[0] = primes[1] = False
        p = 2
        while p * p <= max_n:
            if primes[p]:
                for i in range(p * p, max_n + 1, p):
                    primes[i] = False
            p += 1
        return [i for i, is_prime in enumerate(primes) if is_prime]

    max_n = max(nums)
    primes = sieve(max_n)

    def count_prime_multiples(n, primes):
        count = 0
        is_prime_multiple = [False] * (n + 1)
        for prime in primes:
            if prime > n:
                break
            for multiple in range(prime, n + 1, prime):
                if not is_prime_multiple[multiple]:
                    count += 1
                    is_prime_multiple[multiple] = True
        return count

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        prime_count = count_prime_multiples(n, primes)
        if prime_count % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
