from time import time

start = time()

con = True
i = 1201
while con:
    if len(str(i)) == len(set(str(i))) and str(i)[0] == "1":
        count = 0
        goal = sorted(str(i))
        for j in range(1, 7):
            if sorted(str(i*j)) == goal:
                count += 1
                if count == 6:
                    print(i)
                    con = False
            else:
                break
    i += 1

print("Process took", time() - start, "sec")