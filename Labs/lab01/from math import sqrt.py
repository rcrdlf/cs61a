from math import sqrt
def isPrime(n):
    i = 2
    while i <= int(sqrt(n)):
        if n % i == 0:
            return False
        i = i + 1
    return True

isPrime(89)