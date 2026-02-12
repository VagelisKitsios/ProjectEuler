from time import time
from numpy import sqrt, floor, ceil


def f(x):
    return x*(x+1)


start = time()
z = 3.2e7
two_mil = 2e6
grid_area = 0
Min = two_mil
i = 1
while True:
    y = f(i)
    D = z/y + 1
    x = (sqrt(D) - 1) / 2
    x_prev = floor(x)
    x_next = ceil(x)
    result1 = abs(f(x_prev) * y / 4 - two_mil)
    if result1 < Min:
        Min = result1
        grid_area = x_prev*i
    result2 = abs(f(x_next) * y / 4 - two_mil)
    if result2 < Min:
        Min = result2
        grid_area = x_next*i
    if x_prev <= i:
        print(int(grid_area))
        break
    i += 1

print("Process took", time() - start, "sec")
