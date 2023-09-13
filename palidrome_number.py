num = int(input("enter a number \n"))
reverse = 0
temp = num
while num:
    rem = num % 10
    reverse = reverse * 10 + rem
    num = num // 10
print("the reversed number is", reverse)
if temp == reverse:
    print("this is palindrome")
else:
    print("this is not palindrome")
