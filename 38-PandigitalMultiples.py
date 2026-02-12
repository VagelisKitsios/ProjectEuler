import time

start = time.time()


def is_pandigital(x):
    if "1" in x and "2" in x and "3" in x and "4" in x and "5" in x and "6" in x and "7" in x and "8" in x and "9" in x:
        return True
    return False


max_pan_multiple = 0
for i in range(9123, 9877, 2):
    j = 0
    concatenating_str = ""
    while len(concatenating_str) <= 9:
        j += 1
        concatenating_str += str(i * j)
        if len(concatenating_str) == 9 and is_pandigital(concatenating_str):
            max_pan_multiple = int(concatenating_str)


print(max_pan_multiple)
print("Process took", time.time()-start, "sec")