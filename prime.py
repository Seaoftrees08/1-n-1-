import math
import random

def is_prime(n):
    if n == 1: return False
    if n == 2: return True

    for k in range(100):
        a = random.randint(2, n - 1)

        if gcd(n, a) != 1:
            return False

        if pow(a, n - 1, n) != 1:
            return False

    return True

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

if __name__ == '__main__':
   n = 1
   r = 3
   prod = 2
   while is_prime(prod+1):
      prod *= r
      r += 2
      n += 1
      while not is_prime(r):
         r += 2
   print(str(prod+1) + " is not Prime, n=" + str(n))
      