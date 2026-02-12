import time

start = time.time()


def T_n(n):
    return int(n*(n+1)/2)


def P_n(n):
    return int(n*(3*n - 1)/2)


pen_num_set = set()
tri_hex_num_set = set()
for i in range(287, 56000, 2):
    pen_num_set.add(P_n(i))
    tri_hex_num_set.add(T_n(i))

print(tri_hex_num_set.intersection(pen_num_set))
print("Process took", time.time() - start, "sec")

"""The nth pentagonal number is one third of the (3n − 1)th triangular number. """