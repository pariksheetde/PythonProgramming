a = 12
b = 3

print(a + b)        # 15
print(a - b)        # 9
print(a * b)        # 36
print(a / b)        # 4.0
print(a // b)       # 4
print(a % b)        # 0

print()

for indx in range(0, a // b):
    print(indx)

print()

# BODMAS RULE
print(a + b / 3 - 4 * 12)   # (12 + 1 - 48) = (13 - 48) = -35

# BELOW CODE WILL THROW ERROR
for indx in range(0, a / b):
    print(indx)