arr = []
size = int(input("Enter array size\n"))
print("Enter array elements")
for i in range(size):
    arr.append(int(input()))
sum = sum(arr)
print("Sum of the array =", sum)
