from time import time

f = open("ProjectEuler81.txt", "r")
s = [list(map(int, str(item).strip('\n').split(','))) for item in f.readlines()]
f.close()

start = time()


N = len(s[0])
Dp = [[0] * N for i in range(N)]
for i in range(N):
    Dp[i][0] = s[i][0]
j_coordinates = [0] * N
i = j = 0

while True:
    # Calculate the position of the "active" element with the least cost
    for k in range(N):
        if Dp[k][j_coordinates[k]] < Dp[i][j_coordinates[i]]:
            i = k
    j = j_coordinates[i]

    # Calculate the minimum cost for the above element if it has not already been calculated
    if i > 0:   # If there exists an above element
        key = i - 1
        if Dp[key][j] == 0:
            if j_coordinates[key] < j:
                Dp[key][j] = Dp[i][j] + s[key][j]
                j_coordinates[key] = j

    # Calculate the minimum cost for the below element if it has not already been calculated
    if i != N-1:    # If there exists a below element
        key = i + 1
        if Dp[key][j] == 0:
            if j_coordinates[key] < j:
                Dp[key][j] = Dp[i][j] + s[i + 1][j]
                j_coordinates[key] = j

    # Calculate the minimum cost for the adjacent element.
    # NOTE: The adjacent element could not have already been calculated via another sequence
    if j != N-1:
        Dp[i][j + 1] = Dp[i][j] + s[i][j + 1]
        j_coordinates[i] += 1
    else:   # If the "active" element with the least cost is at the last column then that means that we have
        # calculated the min path value.
        print(Dp[i][j])
        break

print("Process took ", time() - start, " sec.")
