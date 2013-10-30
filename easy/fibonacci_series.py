"""
The Fibonacci series is defined as: F(0) = 0; F(1) = 1; 
F(n) = F(n-1) + F(n-2) when n>1. 
Given a positive integer 'n', print out the F(n).
"""

import sys

# read in from file
input = open(sys.argv[1], 'r')

numbers = []
for line in input:
    numbers.append(line)

input.close()

fib_dict = {}

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if (n-1) in fib_dict:
        n_1 = fib_dict[n-1]
    else:
        n_1 = fib(n-1)
        fib_dict[n-1] = n_1
    if (n-2) in fib_dict:
        n_2 = fib_dict[n-2]
    else:
        n_2 = fib(n-2)
        fib_dict[n-2] = n_2
    return n_1 + n_2

for i, number in enumerate(numbers):
    sys.stdout.write(str(fib(int(number))))
    if i != len(numbers) - 1:
        sys.stdout.write('\n')
