

temperature = 49.87
if temperature <= 32:
    print ("It's freezing!")
elif temperature <=50:
    print("It's cool")
elif temperature <= 75:
    print("It's a little warm")
else:
    print("Ain't that sun a little scorching?")

oski = 54
if oski > 0: 
    print("berkeley")
elif oski < 0:
    print("stanford")
else:
    print('harvard')

from math import sqrt
def isPrime(n):
    i = 2
    while i <= int(sqrt(n)):
        if n % i == 0:
            return False
        i = i + 1

isPrime(7)
isPrime(8)






