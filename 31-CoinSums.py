import time

start = time.time()
coins = [1, 2, 5, 10, 20, 50, 100, 200]

TARGET = 200

matrix = {}
for i in range(TARGET + 1):
    matrix[i, 0] = 1

for i in range(TARGET + 1):
    for j in range(1, len(coins)):
        matrix[i, j] = 0
        if i >= coins[j]:
            matrix[i, j] += matrix[i, j - 1]
            matrix[i, j] += matrix[i - coins[j], j]
        else:
            matrix[i, j] = matrix[i, j - 1]

print(matrix[TARGET, len(coins)-1])

print("Process took", time.time() - start, "sec")
