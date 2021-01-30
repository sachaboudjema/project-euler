"""Largest palindrome product

A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
from math import log10

def is_palindromic_str(n):
    s = str(n)
    if len(s) <= 1:
        return True
    if s[0] == s[-1]:
        return is_palindromic_str(s[1:-1])
    return False


is_pal = is_palindromic_str


def palindromes(start=0, desc=False):
    i = start
    step = -1 if desc else 1
    while True:
        if is_pal(i):
            yield i
        i += step


def prod_of_2_ndigit(i, n):
    for f1 in range(10**(n-1), 10**n):
        if i % f1 == 0:
            f2 = i // f1
            if int(log10(f2)) + 1 == n:
                return (f1, f2)


def largest_pal_with_2_ndigit_factors(n):
    for p in palindromes(start=(10**n-1)**2, desc=True):
        factors = prod_of_2_ndigit(p, n)
        if factors:
            return p, factors

