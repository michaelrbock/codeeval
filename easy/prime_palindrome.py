"""
Write a program to determine the biggest prime palindrome under 1000.
"""

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

def is_palindrome(s):
    return str(s) == str(s)[::-1]

def get_biggest_prime_palindrome(num):
    for i in xrange(num-1, 1, -1):
        if is_prime(i) and is_palindrome(i):
            return i

sys.stdout.write(str(get_biggest_prime_palindrome(1000)))