from decimal import *
from time import time

start = time()
getcontext().prec = 102
total = 0
upper = 100
for i in range(2, upper):
    if (i ** .5).is_integer():
        continue
    s = str(Decimal(i) ** Decimal(1 / 2))
    count = 0
    for j in range(len(s) - 2):
        if s[j] != ".":
            total += int(s[j])
print(total)
print("Process took", time() - start, "sec")
