import time
from itertools import permutations

from sympy import isprime

start = time.time()


def is_pandigital(n):
    digit_num = len(str(n))
    check_set = set()
    for item in range(1, digit_num+1):
        check_set.add(str(item))
    if set(str(n)) == check_set:
        check_set.clear()
        return True
    return False


one_to_nine = "7654321"
max_pandigital_prime = 2143
perm_str = ""
list1 = (list(permutations(one_to_nine)))
for i in list1:
    if i[-1] == "2" or i[-1] == "4" or i[-1] == "5" or i[-1] == "6" or i[-1] == "8":
        continue
    for j in i:
        perm_str += j
    if isprime(int(perm_str)):
        print(perm_str)
        break
    perm_str = ""
print("Process took", time.time() - start, "sec")