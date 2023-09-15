i = int(input("Please Enter Number of rows: "))
j = int(input("Please Enter Number of columns: "))

a = [[0 for _ in range(j)] for _ in range(i)]
b = [[0 for _ in range(j)] for _ in range(i)]
arr = [[0 for _ in range(j)] for _ in range(i)]

print("\nPlease Enter the First Matrix Elements")
for r in range(i):
    for c in range(j):
        a[r][c] = int(input())

print("\nPlease Enter the Second Matrix Elements")
for r in range(i):
    for c in range(j):
        b[r][c] = int(input())

for r in range(i):
    for c in range(j):
        arr[r][c] = a[r][c] * b[r][c]

print("\nThe Multiplication of First Matrix and Second Matrix")
for r in range(i):
    for c in range(j):
        print(arr[r][c], end=" ")
    print()
