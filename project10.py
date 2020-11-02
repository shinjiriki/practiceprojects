# Calculate the sum of digits of a number given by user. E.g.-
# INPUT : 123        OUTPUT : 6
# INPUT : 12345      OUTPUT : 15

# using while
# number = int(input("Input a number: "))
# summ  = 0
# while True:
#     r = number%10
#     number = number/10
#     summ = summ + r
#     if number < 10:
#         summ = summ + number
#         break
# print(int(summ))

# using for
y = 0
number = input("Input a number: ")
for i in number:
    x = int(i)
    x = x + y
    y = x
print(x)

# using function while
# n = int(input("masukkan angka: "))
# def Sum(n):
#     sum = 0
#     while (n>0):
#         sum += int(n%10)
#         n = n/10
#     return sum 
# print(Sum(n))
