from time import time
from itertools import permutations


def is_valid(arr: list, s: str):
    for k in arr:
        if s.index(k[0]) > s.index(k[1]) or s.index(k[1]) > s.index(k[2]):
            return False
    return True


start = time()
replies = []

with open("ProjectEuler79.txt", "r") as fp:
    for i in fp:
        if fp != "\n":
            replies.append(i[:-1])

distinct_digits = set()
for i in replies:
    for j in i:
        distinct_digits.add(j)
distinct_digits = list(distinct_digits)

x = list(permutations(distinct_digits))
for i in x:
    if is_valid(replies, "".join(i)):
        print("".join(i))

print("Process took", time() - start, "sec")
