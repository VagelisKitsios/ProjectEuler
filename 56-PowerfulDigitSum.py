import time

start = time.time()
max_sum = 0
local_sum = 0


def digit_sum(num_str):
    Sum = 0
    for item in num_str:
        Sum += int(item)
    return Sum


for i in range(90, 100):
    for j in range(90, 100):
        x = str(i**j)
        if digit_sum(x) > max_sum:
            max_sum = digit_sum(x)
            print(i, j)

print(max_sum)
print("Process took", time.time() - start, "sec")