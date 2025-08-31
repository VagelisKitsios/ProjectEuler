from time import time

from sympy import isprime

start = time()


def check(k: list, y):
    for el in k:
        if not isprime(int(str(el) + str(y))) or not isprime(int(str(y) + str(el))):
            return False
    return True


def generate_primes(ax=3):
    return (x for x in range(ax, 10000) if isprime(x))


for a in generate_primes():
    for b in generate_primes(a):
        if check([a], b):
            for c in generate_primes(b):
                if check([a, b], c):
                    for d in generate_primes(c):
                        if check([a, b, c], d):
                            for e in generate_primes(d):
                                if check([a, b, c, d], e):
                                    print([a, b, c, d, e], a + b + c + d + e)
                                    print("Process took", time() - start, "sec")
                                    exit()
