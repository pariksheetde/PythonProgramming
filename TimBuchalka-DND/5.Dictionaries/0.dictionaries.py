# DICTONARIES & SETS ARE NOT SEQUENCE. DICTONARIES USE KEY-VALUE PAIR
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
print(f'Type: {type(vehicles)}')
print(f'COntents of Vehicles: {vehicles}')

my_fav_car = vehicles['can-am']
print(f'My dream car: {my_fav_car}')
print()

# use get() to get the value for the corresponding key
desired_car = vehicles.get('roadstar')
print(f'My desired car: {desired_car}')
print()

# use get() to get the value for the corresponding key. If the key is not found, get() retutns None
desired_merc_car = vehicles.get('merc')
print(f'My desired car: {desired_merc_car}')