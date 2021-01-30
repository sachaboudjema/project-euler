"""Even Fibonacci numbers

By considering the terms in the Fibonacci sequence whose values do not exceed
four million, find the sum of the even-valued terms.
"""

def fibs():
    f1 = 0
    f2 = 1
    while True:
        f = f1 + f2
        yield f
        f1 = f2
        f2 = f


def sum_even_fib(n):
    s = 0
    for f in fibs():
        if f % 2 == 0:
            s += f
        if f >= n:
            break
    return s
