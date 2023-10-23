def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)

num1, num2, hcf, lcm = 0, 0, 0, 0
num1, num2 = map(int, input("Enter two integer Values: ").split())
hcf = gcd(num1, num2)
print("GCD:", hcf)
print("LCM:", (num1 * num2) // hcf)
