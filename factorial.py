# Factorial of any number n is represented by n! and is equal to 1*2*3*....*(n-1)*n. E.g.-
# 4! = 1*2*3*4 = 24
# 3! = 3*2*1 = 6
# 2! = 2*1 = 2
# Also,
# 1! = 1
# 0! = 1
# Write a program to calculate factorial of a number.

import math


# using for
print('using for')
x = 1
user = int(input())
if user != 0:
    for i in range(1, user + 1):
        i *= x
        x = i
else:
    i = 1
print(i)

# using while
print('using while')
y = 1
user = int(input())
if user != 0:
    while user > 0:
        y = y * user
        user -= 1
else:
    user = 1
print(y)

# using math.prod
print('using product method')
print(math.prod([i for i in range(1, int(input("Enter a number "))+1)]))

# using math.factorial
print('using factorial method')
print(math.factorial(int(input())))
