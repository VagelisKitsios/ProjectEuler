import time
from math import sqrt
start = time.time()


def prime_factors(n):
    count = 0
    index = 0
    t = [2, 3, 5, 7]
    f = []
    while t[index] <= int(sqrt(n)) + 1:
        count += 1
        if len(t) == (index + 1):
            t.append(t[-2] + 6)
        if n % t[index]:
            index += 1
        else:
            n = n // t[index]
            f.append(t[index])
    if n > 1:
        f.append(n)
    return f


j = 1000
while True:
    j += 1
    if len(set(prime_factors(j))) == len(set(prime_factors(j + 1))) == len(set(prime_factors(j + 2)))\
            == len(set(prime_factors(j + 3))) == 4:
        print(j)
        break
print("Process took", time.time() - start, "sec")
