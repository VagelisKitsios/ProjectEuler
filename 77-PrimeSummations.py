from time import time

from sympy import isprime

start = time()


def prime_summations(n: int, primes_list: list) -> int:
    ways = [1] + [0] * n
    for prime in primes_list:
        for j in range(prime, n + 1):
            ways[j] += ways[j - prime]
    return ways[-1]


primes = []
k = 3
while True:
    if isprime(k-1):
        primes.append(k-1)
    if prime_summations(k, primes) > 5000:
        print(k)
        break
    k += 1
print("Process took", time() - start, "sec")
