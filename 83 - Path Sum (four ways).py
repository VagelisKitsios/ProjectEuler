from time import time
from queue import PriorityQueue

f = open("ProjectEuler81.txt", "r")
s = [list(map(int, str(item).strip('\n').split(','))) for item in f.readlines()]
f.close()

start = time()
"""
s = [[131, 673, 234, 103, 18],
     [201, 96,  342, 965, 150],
     [630, 803, 746, 422, 111],
     [537, 699, 497, 121, 956],
     [805, 732, 524, 37, 331]]"""
N = len(s[0])
Dp = [[0] * N for i in range(N)]
Dp[0][0] = s[0][0]
priorityQueue = PriorityQueue()
priorityQueue.put_nowait((Dp[0][0], 0, 0))

while Dp[N-1][N-1] == 0:
    # Calculate the position of the "active" element with the least cost
    x, i, j = priorityQueue.get_nowait()

    # Calculate the minimum cost for the above element if it has not already been calculated
    if i > 0:   # If there exists an above element
        key = i - 1
        if Dp[key][j] == 0:
            Dp[key][j] = x + s[key][j]
            priorityQueue.put_nowait((Dp[key][j], key, j))

    # Calculate the minimum cost for the below element if it has not already been calculated
    if i != N-1:    # If there exists a below element
        key = i + 1
        if Dp[key][j] == 0:
            Dp[key][j] = x + s[key][j]
            priorityQueue.put_nowait((Dp[key][j], key, j))

    # Calculate the minimum cost for the forward element if it has not already been calculated
    if j != N-1:
        key = j + 1
        if Dp[i][key] == 0:
            Dp[i][key] = x + s[i][key]
            priorityQueue.put_nowait((Dp[i][key], i, key))

    # Calculate the minimum cost for the backwards element if it has not already been calculated
    if j != 0:
        key = j - 1
        if Dp[i][key] == 0:
            Dp[i][key] = x + s[i][key]
            priorityQueue.put_nowait((Dp[i][key], i, key))

print(Dp[N-1][N-1])
print("Process took ", time() - start, " sec.")
