import math
import random

def is_prime(n):
    if n == 1: return False
    if n == 2: return True

    for k in range(50):
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
   r = 3
   prod = 2
   print("3")
   print("")
   while True:
      if is_prime(r):
         prod *= r
         if is_prime(prod+1):
            print(prod+1)
            print("")
      r += 2

      