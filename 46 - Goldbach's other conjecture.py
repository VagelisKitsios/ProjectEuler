import time

start = time.time()


def is_prime(num):
    if num == 2:
        return True
    else:
        for div in range(2, int(num ** .5) + 1):
            if num % div == 0:
                return False
        else:
            return True


odd_composites = []
primes = []
j = 33
while True:
    j += 2
    condition = False
    for k in range(int((j // 2) ** 0.5) + 1):
        if is_prime(j - 2*k**2):
            condition = True
    if not condition:
        print(j)
        break


print("Process took", time.time() - start, "sec")
