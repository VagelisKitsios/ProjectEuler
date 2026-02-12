import time

start = time.time()
Sum = 0
for i in range(2, 354294):
    test = 0
    for j in str(i):
        test += int(j)**5
    if test == i:
        Sum += test

print(Sum)
print("Process took", time.time() - start, "sec")