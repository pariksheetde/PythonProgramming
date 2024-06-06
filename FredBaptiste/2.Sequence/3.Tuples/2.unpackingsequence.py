# UNPACKING SEQUENCES
lst = [10, 20, 30]
a, b, c = lst

print(f'Value of a : {a}')
print(f'Value of b : {b}')
print(f'Value of c : {c}')

print()

rate = (5.1, 5.12)

interest, inflation = rate
print(f'Interest : {interest}')
print(f'inflation : {inflation}')

# UNPACKING TUPLE USING ENEUMERATE
for index in enumerate(range(10,21)):
    id, value = index
    print('ID: {} - Value: {}'.format(id, value))