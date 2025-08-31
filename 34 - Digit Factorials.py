import time
from math import factorial
start = time.time()
Sum = 0
for i in range(3, 50000):
    local_sum = 0
    if "9" in str(i):
        continue
    for digit in str(i):
        local_sum += factorial(int(digit))
        if local_sum == i:
            Sum += i

print(Sum)
print("Process took", time.time() - start, "sec")