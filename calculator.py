num1 = float(input("Enter the First no.: "))
num2 = float(input("Enter the Second no.: "))

op = input("Enter the operator (+,-,*,/): ")

if op == '+':
    print(f"{num1} {op} {num2} = {num1+num2}")
    
elif op == '-':
    print(f"{num1} {op} {num2} = {num1-num2}")
    
elif op == '*':
    print(f"{num1} {op} {num2} = {num1*num2}")
    
elif op == '/':
    print(f"{num1} {op} {num2} = {num1/num2}")
    
else:
    print("Wrong Input, Enter Again")
