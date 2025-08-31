from time import time

start = time()

numerators = [1, 3]
denominators = [1, 2]
count = 0

for i in range(3, 1001):
    denominators.append((denominators[-2] + 2*denominators[-1]))
    numerators.append((numerators[-2] + 2*numerators[-1]))

for i in range(len(numerators)):
    if len(str(numerators[i])) > len(str(denominators[i])):
        count += 1

print(count)
print("Process took", time() - start, "sec")
