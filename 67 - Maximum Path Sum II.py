from time import time


def test(row, index):
    if row == len(lines):
        return 0
    key = str(row) + "|" + str(index)
    if key not in cache:
        cache[key] = lines[row][index] + max(test(row + 1, index), test(row + 1, index + 1))
    return cache[key]


start = time()
lines = []
for line in open("ProjectEuler67.txt").read().strip().split('\n'):
    lines.append(list(map(int, line.split(" "))))

cache = dict()
print(test(0, 0))
print("Process took", time() - start, "sec")
