# Binary Search Algorithm
# Create a random list of numbers between 0 and 100 with a difference of 2 between each number.
# Ask the user for a number between 0 and 100 to check whether their number is in the list.
# The programme should work like this.
# The programme will half the list of numbers and see whether the users number matches the middle element in the list.
# If they do not match, the programme will check which half the number lies in, and eliminate the other half.
# The search then continues on the remaining half,
# again checking whether the middle element in that half is equal to the user’s number.
# This process keeps on going until the programme finds the users number, or until the size of the subarray is 0,
# which means the users number isn't in the list.

import random

guess = int(input("Input a number between 0 and 100 :"))
# number = []
# for i in range(51) :
#     number.append(random.randrange(0, 20, 2))
# simplified to this
number = [random.randrange(0, 100, 2) for i in range(51)]
number.sort()
# half = int(len(number)/2) simplified into
half = len(number)//2
point = number[half]
print(number)
print(f"The Number : {guess}")

while len(number) != 1:
    if guess == point:
        break
    elif guess < point:
        newnumber = number[0:half]
        number = newnumber
    elif guess > point:
        newnumber = number[half+1:len(number)]
        number = newnumber
    if not number:
        break
    half = len(number)//2
    point = number[half]

if guess == point:
    print("Your number exist")
if guess != point:
    print("Your number doesn't exist")
