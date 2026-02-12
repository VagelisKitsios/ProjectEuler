import time

from sympy import isprime, primerange

start = time.time()


primes = list(primerange(2, 1000))
primes.append("K.dot")
max_cons_prime_count = 0
cons_prime_count = 0
values = []
n = 0
for a in range(1, 1000):
    for b in primes:
        while b != primes[-1]:
            n += 1
            x = n**2 + (a*n) + b
            if isprime(x):
                cons_prime_count += 1
            else:
                n = 0
                break
        if cons_prime_count > max_cons_prime_count:
            max_cons_prime_count = cons_prime_count
            values.clear()
            values.insert(0, max_cons_prime_count)
            values.insert(1, a)
            values.insert(2, b)
            values.insert(3, a*b)
        cons_prime_count = 0

        break

for a in range(1, 1000):
    a = -a
    for b in primes:
        while b != primes[-1]:
            n += 1
            x = n**2 + (a*n) + b
            if isprime(x):
                cons_prime_count += 1
            else:
                n = 0
                break
        if cons_prime_count > max_cons_prime_count:
            max_cons_prime_count = cons_prime_count
            values.clear()
            values.insert(0, max_cons_prime_count)
            values.insert(1, a)
            values.insert(2, b)
            values.insert(3, a*b)
        cons_prime_count = 0
print(values)

print("Process took", time.time() - start, "sec")
