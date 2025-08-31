import time

ceiling = 10000

start = time.time()
div_sum = [0]*ceiling
for i in range(1, ceiling//2):
    for j in range(i * 2, ceiling, i):
        div_sum[j] += i


Sum = 0
list1 = list(range(ceiling))
for i in list1:
    a = div_sum[i]
    if a < ceiling and div_sum[a] == i and a != i:
        Sum += a + i
        list1.remove(a)

print(Sum)
print(time.time() - start)
