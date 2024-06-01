EOL = "----"
# Replace any element lesser than 0 with 0 using enumerate() 
data = [10, 20, 30, -10, 40, -5]
for t in enumerate(data):
    index, element = t
    if element <= 0:
        data[index] = 0
print(f'After change : {data}')

print(EOL * 37)

data = [10, 20, 30, -10, 40, -5]
for indx in data:
    if indx <= 0:
        indx = 0
    print(indx)

print(EOL * 37)

# Replace any element lesser than 0 with 0 using enumerate() 
data = [10, 20, 30, -10, 40, -5]
for index, element in enumerate(data):
    if element<=0:
        data[index] = 0
print(data)