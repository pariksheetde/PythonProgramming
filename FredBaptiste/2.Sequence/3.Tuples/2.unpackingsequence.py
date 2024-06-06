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
print()

coffee_table = ("Cappuccino", 100, 75, 34.5)
print('{} was ordered in Table No: {}. Price is {}. Cost of bill was {}'.format(coffee_table[0], coffee_table[1], coffee_table[3], coffee_table[3] * 1.165),'$')
print(f'{coffee_table[0]} was ordered in Table No: {coffee_table[1]}. Price is {coffee_table[3]}. Cost of bill was $ {coffee_table[3] * 1.165}')