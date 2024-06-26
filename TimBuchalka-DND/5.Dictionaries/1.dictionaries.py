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
# solution 1
for key in vehicles:
    print(key, vehicles[key], sep=": ")
print()

# solution 2
for key, value in vehicles.items():
    print(key, value, sep=": ")
print()

# adding new key-value to the dictionary
vehicles["starfighter"] = 'Lockheed F-104'
vehicles["learjet"] = 'Bombardier Learjet 75'
vehicles["toy"] = 'Glider'
print(f"After adding new item in the dictionary: {vehicles}")
print()
