from time import time

from sympy import isprime

start = time()

i = 3
answer = 2
while answer * i <= 1000000:
    answer *= i
    i += 2
    while not isprime(i):
        i += 2

print(answer)
print("Process took", time() - start, "sec")