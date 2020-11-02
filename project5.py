# Password Generator
# Write a programme, which generates a random password for the user.
# Ask the user how long they want their password to be, and how many letters and numbers they want in their password.
# Have a mix of upper and lowercase letters, as well as numbers and symbols.
# The password should be a minimum of 6 characters long.

import random
import string

letstr = string.ascii_letters
numstr = string.digits
stringpass = ""
repeat = False
while not repeat:
    passlen = int(input("How long do you want your password be (Min 6)? "))
    if passlen < 6:
        print("The number you input is too short")
    else :
        while not repeat : 
            letters = int(input("How many letters do you need in a password? "))
            if letters > passlen:
                print("The amount of letters you need exceed the length of a password")
            else:
                numbers = passlen - letters
                # for i in range (letters) :
                #     stringpass += "".join(random.choice(letstr))
                # for i in range (numbers) :
                #     stringpass += "".join(random.choice(numstr))
                stringpass = "".join(random.choice(letstr) for i in range(letters))
                stringpass += "".join(random.choice(numstr) for i in range(numbers))
                passlist = list(stringpass)
                random.shuffle(passlist)
                stringpass = "".join(passlist)
                print(stringpass)
                repeat = True
