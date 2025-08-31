import time
from itertools import permutations


start = time.time()
Sum = 0
pan_str = "1234567890"
pan_list = (list(permutations(pan_str)))
for i in pan_list:
    num = "".join(i)
    if int(num[1:4]) % 2 == 0 and int(num[2:5]) % 3 == 0 and int(num[3:6]) % 5 == 0 and int(num[4:7]) % 7 == 0:
        if int(num[5:8]) % 11 == 0 and int(num[6:9]) % 13 == 0 and int(num[7:10]) % 17 == 0:
            Sum += int(num)

print(Sum)
print("Process took", time.time() - start, "sec")