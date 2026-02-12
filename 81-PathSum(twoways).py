from time import time

t0 = time()

f = open('ProjectEuler81.txt')
s = [list(map(int, str(item).strip('\n').split(','))) for item in f.readlines()]
print(s)
f.close()

N = len(s)
for i in range(N-1, -1, -1):
    for k in range(N-1, -1, -1):
        if i == N-1:
            if k != N-1:
                s[i][k] += s[i][k+1]
        elif k == N-1:
            s[i][k] += s[i+1][k]
        else:
            s[i][k] += min(s[i+1][k], s[i][k+1])
print(s[0][0], time()-t0)
