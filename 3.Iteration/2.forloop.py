EOL = "----"
for indx in range(0,5):
    indx = indx * indx
    print(f'Value : {indx}')
print(EOL * 37)

for i in range(1, 4):
    for j in range(1, i + 1):
        print(i, j, i * j)