from math import gcd
from time import time

start = time()
count = 0
for d in range(3, 12001):
    for n in range(int(d/3)+1, int(d/2)+1):
        if gcd(n, d) == 1:
            count += 1

print(count)
print("Process took", time() - start, "sec")