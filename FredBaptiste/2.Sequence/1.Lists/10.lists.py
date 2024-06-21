# Altering / Changing the elements of the list
marks = [10, 15, 2, 3, 40]
marks[-3:-1] = [20, 25]
# updated_marks = marks[-3:-1]
# updated_marks = [20, 25]
# print(updated_marks)
# print(f'After Change: {updated_marks}')
print(f'After Change, Marks: {marks}')
print()

# Change the last element of the list
grades = [10, 15, 2, 3, 40]
grades[len(grades) - 1] = 4
print(f'New Grade: {grades}')
print()

# delete a specific element in the list
mentos = [10, 1, 20, 30, 35]
del mentos[1]
mentos.insert(4, 40)
print(f'After Change Mentos: {mentos}')
print()

# append() new element, extend() new elements
alpha = [10, 10.5]
alpha.append(20)
alpha.extend([20.5, 30])
print(f'After Change, Alpha: {alpha}')
print()

# extend() new elements
alphabet = ['a', 'b', 'c', 'd', 'e', 'f']
alphabet.extend('ghi')
alphabet.extend(['j','k','l'])
alphabet.extend(('m','n','o'))
print(f'New Alphabet, alphabet: {alphabet}')
print()

# replacing the elements in the list
hector = [1, 20, 30, 5, 6]
del hector[0]
hector[-2:] = [40, 50, 60]
# del hector[0]
print(f'After Change, Hector: {hector}')
print()