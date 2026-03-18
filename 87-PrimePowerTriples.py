from sympy import primerange
from time import time

start = time()
upper_bound = 5e7
square_bound = int(upper_bound**0.5)
cubed_bound = int(upper_bound**(1/3))
fourth_bound = int(upper_bound**.25)
primes = list(primerange(square_bound))

uniq_num = set()
for p1 in primes:
    for p2 in primes:
        if p2 > cubed_bound:
            break
        for p3 in primes:
            if p3 > fourth_bound:
                break
            if p1*p1 + p2**3 + p3**4 < upper_bound:
                uniq_num.add(p1*p1 + p2**3 + p3**4)
            else:
                break

print(len(uniq_num))
print("Process took", time() - start, "sec")
