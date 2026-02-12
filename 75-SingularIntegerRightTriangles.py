from math import sqrt
from time import time

import numpy as np

start = time()
rec = set()
for i in range(1, int(sqrt(750000))+1):
    for j in range(1, i):
        if (i - j) % 2 == 1 and np.gcd(i, j) == 1:
            rec.add(2*i*(i + j))

table = np.zeros(1500001)
for j in rec:
    table[j::j] += 1
print(table.size - np.count_nonzero(table-1))
print("Process took ", time() - start, "sec")
