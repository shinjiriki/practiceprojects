# Take integer inputs from user until he/she presses q ( Ask to press q to quit after every integer input ). 
# Print average and product of all numbers.


y = 0
counter = 0

alphabets = 'abcdefghijklmnoprstuvwxyz'
stop = False

while not stop:
    user = input("Input number : (Press q to quit)\n")
    if user == "q":
        stop = True
        break
    elif user in alphabets:
        print("Please input a number")
    else:
        counter = counter + 1
        x = int(user)
        x = x + y
        y = x
        
print("Total Penjumlahan Input ", x)
print("Total Input ", counter)
print("Rata-rata hasil inputan ", x/counter)
