cart = ['eggs', 'bread', 'ice-cream']
print(cart)

a = b = cart 
print(f'a has : {a}')
print(f'b has : {b}')
# GET THE ID

print(id(cart))
print(id(a))
print(id(b))

print()

odd = [1, 3, 5, 7, 9]
even = [2, 4, 6, 8]
print(f'Max of odd: {max(odd)}')
print(f'Min of odd: {min(odd)}')
print(f'Max of even: {max(even)}')
print(f'Min of even: {min(even)}')
print()

word = 'Mississippi'
print(f'Count of \'s\' : {word.count("s")}')
print()