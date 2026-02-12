from time import time
start = time()


Totient = []
d = 1000001
for i in range(d):
    Totient.append(i)
for i in range(2, d):
    if Totient[i] == i:
        for k in range(i, d, i):
            Totient[k] *= (i - 1)
            Totient[k] //= i

print(sum(Totient[2:]))

print("Process took", time() - start, "sec")
