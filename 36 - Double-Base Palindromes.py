import time

start = time.time()


def is_palindrome(n):
    return str(n) == str(n)[::-1]


Sum = 0
for i in range(1, 1000000, 2):
    if is_palindrome(i) and is_palindrome(int(bin(i)[2::])):
        Sum += i
        print(i)
print(Sum)

print("Process took", time.time() - start, "sec")
