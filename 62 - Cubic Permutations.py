from time import time

start = time()
cubes = []
for i in range(4642, 10000):
    cubes.append(str(i**3))

for i in cubes:
    count = 1
    for j in cubes[cubes.index(i) + 1:None]:
        if len(i) == len(j):
            if sorted(i) == sorted(j):
                count += 1
                if count == 5:
                    print(i)
                    print("Process took ", time() - start, "sec")
                    exit()
        else:
            break
