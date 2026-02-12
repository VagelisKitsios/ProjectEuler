from time import time

from sympy import isprime

start = time()

prime_count = 0
num_count = 1
side_length = 1
skip = 2
n = 1
index = 0
t = 0
while prime_count / num_count >= 0.1 or prime_count == 0:
    for i in range(4):
        n += skip
        num_count += 1
        if isprime(n):
            prime_count += 1
    skip += 2
    side_length += 2
else:
    print(side_length, prime_count/num_count)


print("Process took", time() - start, "sec")