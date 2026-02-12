from random import getrandbits
from time import time
from sympy import primerange
from gmpy2 import is_strong_bpsw_prp as isprime


def main():
    def valid_pair_test(p: int) -> bool:
        for k in primes:
            a = p % k
            if not a or a == (k - 1) // 2:
                return False
        return True

    p = getrandbits(N-1)   # generate a random 2048-bit number
    while p.bit_length() < N-1:
        p = getrandbits(N-1)
    p -= (p % 12) + 1   # a safe prime must be of the form p = 12k - 1
    while True:
        # else if only the pair (p, 2p + 1) is a possible Germain/Safe-prime pair
        if valid_pair_test(p) and isprime(p):
            # 2*p + 1
            if isprime((p * 2) + 1):  # if p is prime and 2p + 1 is also prime then print 2p + 1
                return p*2 + 1
        p += 12


if __name__ == '__main__':
    start = time()
    N = 2048
    primes = tuple(primerange(5, 1420))
    p = main()
    print(p)
    print(p.bit_length())
    print("Process finished in ", (time() - start), "sec.")  # 21.6 sec.
