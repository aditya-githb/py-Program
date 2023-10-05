import math

def convert1(n):
    dec = 0
    i = 0
    while n != 0:
        rem = n % 10
        n //= 10
        dec += rem * pow(2, i)
        i += 1
    return dec

def convert2(n):
    bin = 0
    rem = 0
    i = 1
    while n != 0:
        rem = n % 2
        n //= 2
        bin += rem * i
        i *= 10
    return bin

n = int(input("Enter a binary number: "))
m = int(input("Enter a decimal number: "))

print(f"{n} in binary = {convert1(n)} in decimal")
print(f"{m} in decimal = {convert2(m)} in binary")
