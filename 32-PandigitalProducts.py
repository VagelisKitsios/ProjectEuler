import time

start = time.time()

one_to_nine = {1, 2, 3, 4, 5, 6, 7, 8, 9}
result = set()
sum_set = set()
i = 1234
while i < 9876:
    for j in range(1, 100):
        if i % j == 0 and i % 10 != 0:
            string = str(i) + str(j) + str(int(i // j))
            if len(string) == 9:
                result.clear()
                for item in string:
                    result.add(int(item))
                if result == one_to_nine:
                    sum_set.add(i)
                    i += 1
                    break
    else:
        i += 1


print(sum(sum_set))
print("Process took", time.time()-start, "sec")