string = input("enter any string includes all types of characters: ")
vowel = 0
digit = 0
space = 0
consonant = 0

for char in string:
    if char in ['a', 'e', 'i', 'o', 'u']:
        vowel += 1
    elif char.isdigit():
        digit += 1
    elif char.isspace():
        space += 1
    else:
        consonant += 1

print("vowel =", vowel)
print("digit =", digit)
print("space =", space)
print("consonant =", consonant)
