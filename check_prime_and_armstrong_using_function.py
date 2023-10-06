import math

def checkPrimeNumber(n):
    flag = 1
    squareRoot = int(math.sqrt(n))
    for i in range(2, squareRoot+1):
        if n % i == 0:
            flag = 0
            break
    return flag

def checkArmstrongNumber(num):
    originalNum = num
    remainder = 0
    n = 0
    flag = 0
    result = 0.0
    while originalNum != 0:
        originalNum //= 10
        n += 1
    originalNum = num
    while originalNum != 0:
        remainder = originalNum % 10
        result += math.pow(remainder, n)
        originalNum //= 10
    if round(result) == num:
        flag = 1
    else:
        flag = 0
    return flag

n = int(input("Enter a number: "))
flag = checkPrimeNumber(n)
if flag == 1:
    print(n, "is a prime number.")
else:
    print(n, "is not a prime number.")
flag = checkArmstrongNumber(n)
if flag == 1:
    print(n, "is an Armstrong number.")
else:
    print(n, "is not an Armstrong number.")
