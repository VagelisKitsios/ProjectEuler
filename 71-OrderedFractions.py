from math import gcd
from time import time

start = time()

Max = 2 / 5
answer = None
for d in range(8, 1000000):
    n = int(3 * d / 7)
    while gcd(n, d) != 1:
        n -= 1
        if n / d < Max:
            break
    if n / d > Max:
        Max = n / d
        answer = n

print(answer)
print("Process took", time() - start, "sec")
