from time import time

from sympy import isprime

start = time()

i = 100001
while True:
    if isprime(i):
        for j in range(2):
            if str(j) in str(i)[:-1]:
                count = 0
                for number in range(j, 10):
                    if isprime(int(str(i).replace(str(j), str(number), 3))):
                        count += 1
                    if count == 8:
                        print(i)
                        print("Process took", time() - start, "sec")
                        quit()
                break
    i += 2
