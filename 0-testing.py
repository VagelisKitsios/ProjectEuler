import numpy as np


cards = {0:("w", "w"), 1:("w", "b"), 2:("b", "b")}

n = 10**6
black_black_count = 0
black_count = 0
white_count = 0
for i in range(n):
    card_index = np.random.randint(0, len(cards))
    card_face = np.random.randint(0, 2)
    if cards[card_index][card_face] == "b":
        black_count += 1
        if cards[card_index][0] == "b":
            black_black_count += 1
        else:
            white_count += 1


print(black_black_count/black_count, white_count/black_count)