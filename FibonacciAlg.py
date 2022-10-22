def fibonacci(n):
    if (n < 0):
        return -1
    elif (n == 0 or n == 1):
        return n;
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
 
print("Enter n number inside Fibonacci string: ")
nth = int(input())
fibonacciStr = "";
for i in range(0, nth):
    if i == nth - 1:
        fibonacciStr = fibonacciStr + str(fibonacci(i))
    else:
        fibonacciStr = fibonacciStr + str(fibonacci(i)) + ", "
print(fibonacciStr)