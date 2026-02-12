import time

start = time.time()
Sum = 1
skip = 2
numbers = []
index = 0
add_count = 0
for i in range(3, 1001*1001 + 1):
    numbers.append(i)
try:
    while index <= len(numbers):
        Sum += numbers[index]
        index += skip
        add_count += 1
        if add_count == 3:
            skip += 2
            add_count = -1

except IndexError:
    pass

print(Sum)
print("Process took", time.time() - start, "sec")
