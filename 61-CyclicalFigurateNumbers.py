from time import time

start = time()


def split_number(n):
    return n // 100, n % 100


def make_numbers(formula):
    k = []
    for i in range(19, 142):
        x = int(eval(formula.replace('n', str(i))))
        if 1000 < x:
            k.append(x)
        if x > 10000:
            break
    return k


p3 = [split_number(x) for x in make_numbers('n*(n+1)/2')]
p4 = [split_number(x) for x in make_numbers('n**2')]
p5 = [split_number(x) for x in make_numbers('n*(3*n-1)/2')]
p6 = [split_number(x) for x in make_numbers('n*(2*n-1)')]
p7 = [split_number(x) for x in make_numbers('n*(5*n-3)/2')]
p8 = [split_number(x) for x in make_numbers('n*(3*n-2)')]
all_sets = [p3, p4, p5, p6, p7]


def finder():
    for n1 in p8:
        array = [n1]
        for field2 in all_sets:
            for n2 in field2:
                if n2[0] == n1[1] and n2 not in array:
                    used = [p8, field2]
                    array = [n1, n2]
                    for field3 in all_sets:
                        if field3 not in used:
                            for n3 in field3:
                                if n3[0] == n2[1] and n3 not in array:
                                    used = [p8, field2, field3]
                                    array = [n1, n2, n3]

                                    for field4 in all_sets:
                                        if field4 not in used:
                                            for n4 in field4:
                                                if n4[0] == n3[1] and n4 not in array:
                                                    used = [p8, field2, field3,
                                                            field4]
                                                    array = [n1, n2, n3, n4]

                                                    for field5 in all_sets:
                                                        if field5 not in used:
                                                            for n5 in field5:
                                                                if n5[0] == n4[1] \
                                                                        and n5 not in array:
                                                                    used = [p8,
                                                                            field2, field3, field4, field5]
                                                                    array = [n1, n2, n3, n4, n5]

                                                                    for field6 in all_sets:
                                                                        if field6 not in used:
                                                                            for n6 in field6:
                                                                                if n6[0] == n5[1] \
                                                                                        and n6[1] == n1[0] \
                                                                                        and n6 not in array:
                                                                                    return \
                                                                                        [n1, n2, n3, n4, n5, n6]


def p61():
    return sum([el[0] * 100 + el[1] for el in finder()])


print(p61())

print("Process took ", time() - start, "sec")