import time

from sympy import isprime

start = time.time()

most_consecutive_primes = 6
primes = [2]

for i in range(3, 9000, 2):
    if isprime(i):
        primes.append(i)

j = 0
k = -1
max_row = 21
for j in range(5):
    k = -1
    while abs(k) + j < len(primes):
        if sum(primes[j:k]) < 1000000 and isprime(sum(primes[j:k])) and len(primes[j:k]) > max_row:
            max_row = len(primes[j:k])
            print(max_row, sum(primes[j:k]), k, j)
        k -= 1


print("Process took", time.time() - start, "sec")
