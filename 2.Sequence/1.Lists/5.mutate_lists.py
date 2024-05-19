EOL = "----"
lst = [10, 20, 30]
lst[1] = 'Python'
print(f'After Change : {lst}')

print(EOL * 37)


marks = [10, 20, 30, 40, 50]
print(f'Before Change : {marks}')
marks[0:2] = ['SQL', 'Python', 'AWS']
print(f'After Change : {marks}')

print(EOL * 37)

# APPEND
lst = [10, 20, 30]
lst.append(40)
print(f'After appending new elements : {lst}')

print(EOL * 37)

# EXTEND 
var = [10, 20, 30]
var.extend([40])
print(f'After extending new elements : {var}')

print(EOL * 37)

# INSERT
val = [10, 20, 30]
val.insert(0, 100)
print(f'After inseting new element : {val}')

print(EOL * 37)

# EXTEND
age = [10, 20, 30]
age.extend([40, 50])
age.extend((60, 70))
print(f'After extending new elements Age : {age}')

print(EOL * 37)