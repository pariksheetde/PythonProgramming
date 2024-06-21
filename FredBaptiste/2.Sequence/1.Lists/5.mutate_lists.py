
lst = [10, 20, 30]
lst[1] = 'Python'
print(f'After Change : {lst}')
print()


marks = [10, 20, 30, 40, 50]
print(f'Before Change : {marks}')
marks[0:2] = ['SQL', 'Python', 'AWS']
print(f'After Change : {marks}')
print()

# APPEND
lst = [10, 20, 30]
lst.append(40)
print(f'After appending new elements : {lst}')
print()

# EXTEND 
var = [10, 20, 30]
var.extend([40])
print(f'After extending new elements : {var}')
print()

# INSERT
val = [10, 20, 30]
val.insert(0, 100)
print(f'After inseting new element : {val}')
print()

# EXTEND
age = [10, 20, 30]
age.extend([40, 50])
age.extend((60, 70))
print(f'After extending new elements Age : {age}')
print()

dep = [10, 20, 3, 40, 50]
dep[1:3] = (2, 3, 4)
print(f'Type : {type(dep)}', dep)
print()

sd = [10, 20, 3, 40, 50]
sd[1:3] = 'python'
print(f'After change : {sd}')
print()

age = [1, 2, 3, 4, 5, 6, 7, 8]
print(f'Before change : {age[1::2]}')
age[1::2] = (20, 40, 60, 80)
print(f'After change : {age}')
print()

aldo = [10, 20, 30, 40, 50, 60]
print(f'Before change "Aldo" : {aldo}')
print(aldo[1:3])
aldo[1:3] = [0, 1, 2]
print(f'After change "Aldo" : {aldo}')
print()

lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
lst[:-6:-1]
print(f'After 1st change : {lst[:-6:-1]}')
lst[:-6:-1] = [90, 80, 70, 60, 50]
print(f'After 2nd change : {lst}')
print()

# APPEND
pde = [1, 2, 3]
pde.append(4)
pde.append([5, 6, 7])
pde.extend([8, 9, 10])
print(f'After appending : {pde}')
print()