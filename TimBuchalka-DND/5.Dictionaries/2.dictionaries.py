vehicles = {
    'dream' : 'Honda 250T',
    'roadstar' : 'BMW R1100',
    'er5' : 'Kawasaki ER5',
    'can-am' : 'Bombardier Can-Am 250',
    'virago' : 'Yamaha XV250',
    'tenere' : 'Yamaha XT650',
    'jimny' : 'Suzuki Jimny 1.5',
    'fiesta' : 'Ford Fiesta Ghia 1.4',
}
# adding new key-value pair to the existing dictionary
vehicles['stafighter'] = 'Lockheed F-184'
vehicles['learjet'] = 'Bombardier Learjet 75'
vehicles['toy'] = 'Glider'
vehicles['virago'] = 'Yamaha XV750'

for key, value in vehicles.items():
    print(key.title(), value, sep=': ')
print()

# delete key-value from existing dictionary
del vehicles["can-am"]
for key, value in vehicles.items():
    print(key.title(), value, sep=': ')
print()