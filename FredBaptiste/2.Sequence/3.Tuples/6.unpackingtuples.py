# unpacking tuples
data = (1, 2, 3)
a, b, c = data
print(f'Value of A: {a}')
print(f'Value of B: {b}')
print(f'Value of C: {c}')
print()

rate = 5.15, 5.12
apr, apy = rate
print(f'APR: {apr}')
print(f'APY: {apy}')
print()

rate = 5.15, 5.12
apr, apy = rate
# let's swap the values using temp variable
temp = apy
apy = apr
apr = temp

print(f'APR: {apr}')
print(f'APY: {apy}')
print()

# unpacking tuples
x, y, z = 'ABC', 'XYZ', 'PQR'
print(x)
print(y)
print(z)
print()
