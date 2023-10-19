def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

num = int(input("Enter the number: "))
f = factorial(num)
print("Factorial of the number is", f)
