def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)

# Call fib(5) and print the result
print(fib(5)) #output fib(5)=5

