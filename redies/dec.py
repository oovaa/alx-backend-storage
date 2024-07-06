

import time


def timer(f):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = f(*args, **kwargs)
        end = time.time()
        dt = end - start
        print(f"{dt} ms")
        return res
    return wrapper


@timer
def prime_factorizataion(n):
    factors = []
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1

    return factors


print(prime_factorizataion(2**29 + 1))
