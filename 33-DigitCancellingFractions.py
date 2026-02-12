import time

start = time.time()


def simplify_fractions(num, den):
    gcd = 1
    for x in range(1, min(num, den)//2 + 1):
        if num % x == 0 and den % x == 0:
            gcd = x
    return (num // gcd) / (den//gcd)


def is_trivial(ar, par):
    if ar % 10 != 0 and par % 10 != 0:
        return True
    else:
        return False


den_prod = 1
num_prod = 1
key_fractions = list()
for i in range(11, 100):
    for j in range(10, i):
        if is_trivial(j, i) and str(i)[0] != str(j)[0]:
            if len(str(simplify_fractions(j, i))) <= 4:
                for letter in str(i):
                    if letter in str(j):
                        final = str(j).replace(letter, "") + "/" + str(i).replace(letter, "")
                        if simplify_fractions(j, i) == eval(final):
                            den_prod *= int(str(i).replace(letter, ""))
                            num_prod *= int(str(j).replace(letter, ""))

print(den_prod/num_prod)
print("Process took", time.time() - start, "sec")