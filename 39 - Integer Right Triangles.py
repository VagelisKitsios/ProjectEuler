from math import sqrt
from time import time

start = time()


def pythagorean_triplet(n):
    count = 0
    i = 1
    while i != int(n / 3) + 1:
        for j in range(i + 1, int(n / 2) + 1):
            k = n - i - j
            if i * i + j * j == k * k:
                count += 1
        i += 1
    return count


side_a = []
list1 = list()
max_solutions = 0
wanted_perimeter = 0
for a in range(2, 500, 2):
    side_a.append(a)
side_b = side_a.copy()


for b in side_b:
    for a in side_a:
        c = (sqrt(b**2+a**2))
        if c == int(c) and 210 < a+b+c <= 1000:
            list1.append(int(a+b+c))

list1 = list(set(list1))

for i in list1:
    if pythagorean_triplet(i) > max_solutions:
        max_solutions = pythagorean_triplet(i)
        wanted_perimeter = i
print(wanted_perimeter)
print("Process took", time() - start, "sec")