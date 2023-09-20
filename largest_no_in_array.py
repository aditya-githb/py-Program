num = int(input("Enter the number of elements (1 to 100): "))
arr = []
for i in range(num):
    arr.append(float(input("Enter number {}: ".format(i + 1))))

largest_element = max(arr)
print("Largest element = {:.2f}".format(largest_element))
