from time import time
from math import log

start = time()
lines = []
Max = 1
Max_i = 0
i = 1
for line in open("99_base_exp.txt").read().strip().split('\n'):
    base_exp = line.split(",")
    base = int(base_exp[0])
    exp = int(base_exp[1])
    if exp*log(base) > Max:
        Max_i = i
        Max = exp*log(base)
    i += 1
print(Max_i)
print("Process took", time() - start, "sec")