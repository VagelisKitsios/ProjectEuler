import time

start = time.time()
set1 = set()

for a in range(2, 101):
    for b in range(2, 101):
        set1.add(pow(a, b))

print(len(set1))
print("Process took", time.time() - start, "sec")