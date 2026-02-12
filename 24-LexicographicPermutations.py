import time
from itertools import permutations

start = time.time()
numbers = "0123456789"

list1 = (list(permutations(numbers)))
print("".join(list1[999999]))

print("Process took", time.time()-start, "sec")
