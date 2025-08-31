from time import time
import numpy as np
start = time()

N = 40
dice_prob = (1 / 16, 1 / 8, 3 / 16, 1 / 4, 3 / 16, 1 / 8, 1 / 16)
P = np.zeros(shape=(N, N))

for square in range(N):     # square -> starting square before the dice roll
    for j in range(len(dice_prob)):
        key = j + 2 + square
        if key >= N:    # Reset key value so that key < 40
            key %= N
        prob_j_div_16 = dice_prob[j] / 16    # To reuse later
        prob_j_div_8 = dice_prob[j] / 8      # To reuse later
        if key == 2 or key == 17 or key == 33:
            # If we land on a Community Chest square then, there is a 7/8 chance that we remain on that square and a
            # 1/8 chance that we go to square 0 or square 10
            P[square][key] += dice_prob[j] * 7 / 8
            P[square][0] += prob_j_div_16
            P[square][10] += prob_j_div_16
        elif key == 30:     # If we land on square 30 then we are being taken to jail which is square 10
            P[square][10] += dice_prob[j]
        elif key == 7 or key == 22 or key == 36:
            # If we land on a Chance square there is a 3/8 chance that we remain on that square and a 5/8 chance that
            # we are being transferred to one of the squares below
            P[square][key] += prob_j_div_8 * 3
            P[square][0] += prob_j_div_16
            P[square][11] += prob_j_div_16
            P[square][10] += prob_j_div_16
            P[square][24] += prob_j_div_16
            P[square][39] += prob_j_div_16
            P[square][5] += prob_j_div_16
            P[square][key - 3] += prob_j_div_16
            if key == 7:
                P[square][15] += prob_j_div_8
                P[square][12] += prob_j_div_16
            elif key == 22:
                P[square][25] += prob_j_div_8
                P[square][28] += prob_j_div_16
            else:
                P[square][12] += prob_j_div_16
                P[square][5] += prob_j_div_8
        else:
            P[square][key] += dice_prob[j]


# Multiply matrix P with itself until it converges to a matrix with at least 4 decimal accurate digits in every element.
P_prev = P.copy()
while True:
    P_next = P_prev @ P
    if np.linalg.norm(P_next[0] - P_prev[0], np.inf) <= 1e-4/2:
        break
    P_prev = P_next

# print the answer
copy_array = P_next[0].copy()
for i in range(3):
    Max = 0
    Max_index = 0
    for k in range(copy_array.size):
        if copy_array[k] > Max:
            Max = copy_array[k]
            Max_index = k
    print(Max_index, Max)
    copy_array[Max_index] = 0

print("Process took ", time() - start, " sec.")