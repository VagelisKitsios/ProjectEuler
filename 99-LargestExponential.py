def foo(u: int) -> float:
    S = 0
    for i in range(1, 10):
        S += i**3 * (10-i)**7
    return (u**3*(10-u)**7)/S

Sum = 0
for u in range(11):
    Sum += foo(u)
    print(u, foo(u))
print(Sum)
