import time

start = time.time()


def cycle_length(n):
    d = 10 ** len(str(n))
    r = []
    for i in range(d * 10 + 1):
        r.append(-1)
    r[d] = 1
    j = 1
    while d % n != 0:
        j += 1
        d = (d % n) * 10
        if r[d] != -1:
            return j - r[d]
        r[d] = j
    return 0


ans = [0, 0]
for i in range(1, 1000):
    c = cycle_length(i)
    if c > ans[1]:
        ans = [i, c]

print(ans)
print("Process took", time.time() - start, "sec")
