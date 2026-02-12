import time

from sympy import isprime

start = time.time()

Sum = 0
for i in range(11, 1000000, 2):
    if "2" in str(i) or "4" in str(i) or "5" in str(i) or "6" in str(i) or "8" in str(i) or "0" in str(i):
        continue
    if isprime(i):
        key = str(i)
        for j in range(1, len(str(i))):
            if isprime(int(key[:-j])) and isprime(int(key[j:])):
                if j == len(key) - 1:
                    Sum += i
            else:
                break

print(Sum)
print("Process took", time.time() - start, "sec")