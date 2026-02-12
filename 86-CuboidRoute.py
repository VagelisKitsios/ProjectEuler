from time import time
from sympy import gcd


def count_triplet_combinations(a: int, b: int, LIMIT: int) -> int:
    L_a = LIMIT // a
    result = (L_a*(b // 2)*(1 + L_a)) // 2
    if b % 2 == 1:
        k = L_a // 2
        result += k * (k + 1) - ((L_a+1) % 2) * k
    if b - a > 1:
        result -= (L_a * (b - a + L_a * (b - a)))//2 - L_a
    elif b - a == 1:
        result -= ((((b-a) * 2)+L_a*(b-a))*(L_a - 1) // 2) - L_a + 1
    return result


def triplet_count_up_to(LIMIT: int) -> int:
    result = 0
    end_i = int((2*LIMIT)**.5) + 1
    for i in range(2, end_i):
        for j in range(1 + i % 2, min(i, int(LIMIT/i) + 1), 2):
            a = i*i
            b = j*j
            y = 2*i*j
            x = a - b
            if gcd(i, j) == 1:
                if (x << 1) > y:
                    result += count_triplet_combinations(x, y, LIMIT)
                if (y << 1) > x:
                    result += count_triplet_combinations(y, x, LIMIT)

    return result


start = time()
upper_bound = 10000
lower_bound = 100
while True:
    M = (upper_bound + lower_bound)//2
    if triplet_count_up_to(M) > 1e6:
        if triplet_count_up_to(M-1) <= 1e6:
            break
        else:
            upper_bound = M
    else:
        lower_bound = M


print(M)

print("Process took", time() - start, "sec")
