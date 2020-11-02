# Write a program to print a number given by user but digits reversed. E.g.-
# INPUT : 123        OUTPUT : 321
# INPUT : 12345      OUTPUT : 54321


user = input('Input a number : ')
user = ''.join(str(i) for i in range(len(user), 0, -1))
print(user)
