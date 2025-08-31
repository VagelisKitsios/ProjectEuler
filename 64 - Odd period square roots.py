from time import time

start = time()
odd_counter = 0
for i in range(2, 1001):
    s = i**.5
    if s != int(s):
        b = []
        count = 0
        m = 0
        d = 1
        a = int(s)
        while a != 2*int(s):
            m = d*a - m
            d = (i - m**2)/d
            a = int((s + m)/d)
            count += 1
            b.append(a)
        print(b)
        if count % 2 == 1:
            odd_counter += 1

print(odd_counter)
print("Process took ", time() - start, "sec")
