for index in range(0,11):
    if index % 2 == 0:
        print(f'Square of {index}: {index ** 2}')

print()

for index in range(0,11):
    if index % 2 == 0:
        print("Square of {0:2}: {1:2} cube of {2:3}: {3}".format(index, index ** 2, index, index ** 3))

print()

for index in range(0,11):
        print("Square of {0:2}: {1:<2} cube of {2:<3}: {3}".format(index, index ** 2, index, index ** 3))

print()

print("PI is approximately: {0:5f}".format(22/7))
print("PI is approximately: {0:10f}".format(22/7))
print("PI is approximately: {0:15f}".format(22/7))
print("PI is approximately: {0:20f}".format(22/7))
print("PI is approximately: {0:25f}".format(22/7))

print()