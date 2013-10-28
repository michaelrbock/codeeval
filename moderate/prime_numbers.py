import math
import sys

input = open(sys.argv[1], 'r')

nums = []

for line in input:
    nums.append(int(line))

input.close()

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

for i, num in enumerate(nums):
    primes = []
    for j in range(2, num):
        if is_prime(j):
            primes.append(j)
    for k, prime in enumerate(primes):
        sys.stdout.write(str(prime))
        if k != len(primes) - 1:
            sys.stdout.write(',')
    if i != len(nums) - 1:
        sys.stdout.write('\n')
