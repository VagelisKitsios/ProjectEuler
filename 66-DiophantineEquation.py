from time import time

start = time()

Max = 9
answer = 5

for i in range(5, 1001):
    s = i ** .5
    c = int(s)
    if s != c:
        convergent_ratio = []
        m = 0
        d = 1
        a = int(s)
        while a != 2 * int(s):
            m = d * a - m
            d = (i - m ** 2) / d
            a = int((s + m) / d)
            convergent_ratio.append(a)
        x = convergent_ratio[0]
        convergent_ratio.append(x)
        convergent_ratio.pop(0)
        solution_found = False
        numerator_0 = c
        numerator_1 = numerator_0 * x + 1
        denominator_0 = 1
        denominator_1 = x
        while not solution_found:
            for j in convergent_ratio:
                n = numerator_1
                numerator_1 = j * numerator_1 + numerator_0
                numerator_0 = n
                p = denominator_1
                denominator_1 = j * denominator_1 + denominator_0
                denominator_0 = p
                if numerator_0**2 - i*(denominator_0 ** 2) == 1:
                    solution_found = True
                    if numerator_0 > Max:
                        answer = i
                        Max = numerator_0
                    break

print(answer)
print("Process took ", time() - start, "sec")
