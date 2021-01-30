"""Largest prime factor

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""
from math import sqrt


def is_prime(n):
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i**2 <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def primes():
    p = 2
    while True:
        if is_prime(p):
            yield p
        p += 1


def prime_factors(n):
    f = 2
    while not is_prime(n):
        for p in primes():
            if n % p == 0:
                f = p
                n = n // p
                yield p
                break
    yield n

