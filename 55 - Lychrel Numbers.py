from time import time

start = time()


def is_palindrome(n):
    return str(n) == str(n)[::-1]


def is_Lychrel_num(n):
    iterations = 0
    while iterations <= 49:
        iterations += 1
        n += int(str(n)[::-1])
        if is_palindrome(n):
            return False
    return True


count = 0
for i in range(10, 10000):
    if is_Lychrel_num(i):
        count += 1
print(count)
print(len(str(100**100)))
print("Process took", time() - start, "sec")