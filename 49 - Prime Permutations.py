import time

from sympy import isprime

start = time.time()


for i in range(1489, 10000, 2):
    check_if_perm = set()
    j = 1000
    if isprime(i):
        while j+j+i < 10000:
            if sorted(str(i)) == sorted(str(i+j)) == sorted(str(i+j+j)) and isprime(i+j) and isprime(i+j+j):
                print(str(i)+str(i+j)+str(i+j+j), j)
                print("Process took", time.time() - start, "sec")
                exit()
            j += 10
