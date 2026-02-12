from time import time

from sympy import isprime

start = time()

primes = []
for i in range(1001, 10**4, 2):
    if isprime(i):
        primes.append(i)
Min = 3
answer = None
for i in range(len(primes)-1):
    for j in range(i+1, len(primes)):
        n = primes[i]*primes[j]
        if n > 10**7:
            break
        fn = (primes[i]-1)*(primes[j]-1)
        ratio = n / fn
        if ratio < Min and fn % 3 == n % 3:
            if sorted(str(fn)) == sorted(str(n)):
                Min = ratio
                answer = n

print(answer)
print("Process took", time() - start, "sec")