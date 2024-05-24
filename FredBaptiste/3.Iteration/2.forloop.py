EOL = "----"
for indx in range(0,5):
    indx = indx * indx
    print(f'Value : {indx}')

print(EOL * 37)

for i in range(1, 4):
    for j in range(1, i + 1):
        print(i, j, i * j)

print(EOL * 37)

# Replace any element lesser than 0 with 0 
data = [10, 20, 30, -10, 40, -5]
for indx in data:
    if indx < 0:
        indx = 0
    print(indx)