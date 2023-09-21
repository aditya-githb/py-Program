def recSum(n):
    if n:
        return n + recSum(n - 1)
    else:
        return n

num = int(input("Enter a positive number to get the sum: "))
print("\nThe Sum is:", recSum(num))
