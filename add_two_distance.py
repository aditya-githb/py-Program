class Distance:
    def __init__(self):
        self.feet = 0
        self.inch = 0.0

d1 = Distance()
d2 = Distance()
result = Distance()

print("Enter 1st distance")
print("Enter feet: ")
d1.feet = int(input())
print("Enter inch: ")
d1.inch = float(input())

print("\nEnter 2nd distance")
print("Enter feet: ")
d2.feet = int(input())
print("Enter inch: ")
d2.inch = float(input())

result.feet = d1.feet + d2.feet
result.inch = d1.inch + d2.inch

while result.inch >= 12.0:
    result.inch = result.inch - 12.0
    result.feet += 1

print("\nSum of distances = %d\'-%.1f\"" % (result.feet, result.inch))
