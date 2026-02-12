from time import time
start = time()

k = 2
a = 2
b = 3
c = None

for i in range(98):
    if i % 3 != 0:
        c = a + b
    else:
        c = a + k*b
        k += 2
    a = b
    b = c
Sum = 0
for i in range(len(str(c))):
    Sum += int(str(c)[i])

print(Sum)
print(c)
print("Process took", time() - start, "Sec")