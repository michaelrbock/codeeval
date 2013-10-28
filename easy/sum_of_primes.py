import math
import sys

def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    m = int(math.sqrt(num))
    for i in range(3, m+1, 2):
        if num % i == 0:
            return False
    return True

sum = 0
i = 1
num_primes = 0

# this could take a while...
while num_primes < 1000:
    if is_prime(i):
        sum += i
        num_primes += 1
    i += 1

sys.stdout.write(str(sum))
