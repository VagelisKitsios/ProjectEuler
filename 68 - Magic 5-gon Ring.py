from itertools import permutations
from time import time

start = time()

A = list(permutations([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
Max_solution = 0
for i in range(len(A)):
    if A[i][1] != 10 and A[i][2] != 10 and A[i][4] != 10 and A[i][6] != 10 and A[i][8] != 10:
        pentagon = [[A[i][0], A[i][1], A[i][2]], [A[i][2], A[i][3], A[i][4]], [A[i][4], A[i][5], A[i][6]], [A[i][6], A[i][7], A[i][8]], [A[i][8], A[i][9], A[i][1]]]
        target_sum = sum(pentagon[0])
        is_solution = True
        for j in range(1, 5):
            if sum(pentagon[j]) != target_sum:
                is_solution = False
                break
        if is_solution:
            Min_node = pentagon[0][0]
            external_min_index = 0
            for j in range(1, 5):
                if pentagon[j][1] < Min_node:
                    Min_node = pentagon[j][1]
                    external_min_index = j

            concatenated = ""
            for j in range(external_min_index, 5):
                if j == 0:
                    concatenated += str(pentagon[0][0]) + str(pentagon[0][1]) + str(pentagon[0][2])
                else:
                    concatenated += str(pentagon[j][1]) + str(pentagon[j][0]) + str(pentagon[j][2])
            for j in range(external_min_index):
                if j == 0:
                    concatenated += str(pentagon[0][0]) + str(pentagon[0][1]) + str(pentagon[0][2])
                else:
                    concatenated += str(pentagon[j][1]) + str(pentagon[j][0]) + str(pentagon[j][2])
            concatenated = int(concatenated)
            if concatenated > Max_solution:
                Max_solution = concatenated

print(Max_solution)

print("Process took", time() - start, "sec")