import time

start = time.time()


def Pn(n):
    return (n*((3*n)-1))/2


def is_pentagonal_num(x):
    return ((((24*x)+1)**.5 + 1)/6).is_integer()


for i in range(8, 2999, 2):
    for j in range(7, 3000, 2):
        x = Pn(i) + Pn(j)
        z = abs(Pn(i) - Pn(j))
        if is_pentagonal_num(x) and is_pentagonal_num(z):
            print(z, x, z, i, j)
            print("Process took", time.time() - start, "sec")
            exit()
        else:
            continue


