from time import time

start = time()
TARGET = 100


matrix = {}
for i in range(TARGET + 1):
    matrix[i, 0] = 1

for i in range(TARGET + 1):
    for j in range(1, TARGET-1):
        matrix[i, j] = 0
        if i >= j + 1:
            matrix[i, j] += matrix[i, j - 1]
            matrix[i, j] += matrix[i - j - 1, j]
        else:
            matrix[i, j] = matrix[i, j - 1]

print(matrix[TARGET, TARGET-2])

print("Process took", time() - start, "sec")
