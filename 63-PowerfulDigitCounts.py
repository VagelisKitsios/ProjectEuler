from time import time

start = time()
count = 0
for i in range(1, 10):
    for j in range(1, i+19):
        if j == len(str(i**j)):
            count += 1
            print(i, j)
print(count)
print("Process took ", time() - start, "sec")
