# Even Fibonacci numbers
# Each new term in the Fibonacci sequence is generated by adding the previous two terms.
# By starting with 1 and 2, the first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# by considering the terms in the Fibonacci sequence whose values do not exceed four million,
# find the sum of the even-valued terms.

y = 0
z = 1
w = 0
for x in range(0, 10):
    x = y 
    y = z
    z = x + y
    w = z + w
    print(z)
print("The sum of the fibonacci above would be : ", w)


fibonacciSeries = [1,2]
N = 10
if N > 2:
    for i in range(2, N):
        nextElement = fibonacciSeries[i-1] + fibonacciSeries[i-2]
        fibonacciSeries.append(nextElement)
print("The fibonacci series would be : ", fibonacciSeries)
print("The fibonacci series would be : ", sum(fibonacciSeries))