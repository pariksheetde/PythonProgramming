# SORTED METHOD
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]
numbers = sorted(even + odd)
print("Concatenating {} & {} : {}".format(even, odd, numbers))
print()

# EXTEND & SORT METHOD
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]
odd.extend(even)
odd.sort()
print("Using extend() method :{}".format(odd))
print()

# SORTED METHOD
digits = sorted("432985617")
print("Digits : {}".format(digits))
print()

# COPY METHOD
age = [2, 4, 6, 8, 10, 12]
copy = age.copy()
print("Age : {}".format(age))
print("Copy : {}".format(copy))
print(age is copy)
print(age == copy)
print()

computer_parts = ['computer', 'monitor', 'keyboard', 'mouse', 'mouse mat']
computer_parts[-1] = 'track ball'
print("After replacing existing element in the list {}".format(computer_parts))
print()

# REPLACING all the elements in the list
games = ['midtown madness', 'project igi', 'max payne', 'mafia']
games[:] = ['Asphault 8']
print("New Games: {}".format(games))
print()

# DELETE elements from the list
data = [4, 5, 104, 101, 111, 113, 107, 109, 100, 107, 114]
del data[:2]
print("After deleting the elements {}:".format(data))
print()