from time import time

start = time()

repeats = {169, 363601, 1454, 871, 45361, 872, 45362, 1, 2, 145, 40585}
checked = dict()


sixty_chain_count = 0


def factorial_digit_sum(n):
    factorials = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
    result = 0
    for k in str(n):
        result += factorials[int(k)]
    return result


for i in range(3, 1000001):
    s = str(i)
    perm = "".join(sorted(s))
    if perm in checked:
        sixty_chain_count += checked.get(perm)
    else:

        count = 1
        x = factorial_digit_sum(i)
        while x not in repeats:
            count += 1
            x = factorial_digit_sum(x)

        if count == 57:
            sixty_chain_count += 1
        checked[perm] = count // 57
print(sixty_chain_count)

print("Process took ", time() - start, "sec")
