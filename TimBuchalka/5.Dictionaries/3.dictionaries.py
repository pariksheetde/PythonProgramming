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
# pop() to delete key
unwanted= vehicles.pop("can-am", "Specified key doesn't exist")
print(f'Key to be deleted: {unwanted}')

# pop() to delete key
unavailable_key= vehicles.pop("merc", "Specified key doesn't exist")
print(f'Key to be deleted: {unavailable_key}')

print()