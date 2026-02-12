import time

start = time.time()


def is_prime(num):
    for div in range(2, int((num ** .5) + 1)):
        if num % div == 0:
            return False
    else:
        return True


circular_prime_count_set = {2, 5}
cycle = []
for i in range(3, 1000000, 2):
    if "2" in str(i) or "4" in str(i) or "5" in str(i) or "6" in str(i) or "8" in str(i) or "0" in str(i):
        continue
    if is_prime(i):
        cycle.clear()
        for item in str(i):
            cycle.append(item)
        count = 0
        for rotations in range(len(cycle)):
            cycle.append(cycle[0])
            cycle.pop(0)
            if is_prime(int("".join(cycle))):
                count += 1
            if count == len(cycle):
                circular_prime_count_set.add(i)
                break

print(len(circular_prime_count_set))
print("Process took", time.time() - start, "sec")
