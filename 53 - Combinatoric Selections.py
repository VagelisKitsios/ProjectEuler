from math import factorial
from time import time
start = time()


def number_of_combinations(n, limit):
    return factorial(n)/(factorial(limit)*(factorial(n-limit)))


count = 0
for i in range(1, 101):
    for j in range(2, i-2):
        if number_of_combinations(i, j) > 1000000:
            count += 1
print(count)
print("Process took", time() - start, "sec")