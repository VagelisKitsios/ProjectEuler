from time import time

start = time()
P = [1, 1]
d = 1000000
n = 1
while True:
    n += 1
    P.append(0)
    i = 0
    while True:
        i += 1
        m1 = n - i*(3*i - 1)/2
        m2 = n - i*(3*i + 1)/2
        s = 1
        if i % 2 == 0:
            s = -1
        if m1 >= 0:
            P[n] += s * P[int(m1)]
        if m2 >= 0:
            P[n] += s * P[int(m2)]
        if m1 < 0 and m2 < 0:
            break
    P[n] = P[n] % d
    if P[n] == 0:
        break
print(n)
print("Process took", time() - start, "sec")