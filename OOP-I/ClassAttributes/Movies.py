class Movie:
    id_counter = 0
    def __init__(self, title, year):
        self.id = Movie.id_counter
        self.title = title
        self.year = year

        Movie.id_counter += 1

venom = Movie("Venom", 2018)
print(f'ID: {Movie.id_counter}. {venom.title} was released in the year {venom.year}')

mib = Movie("MIB", 2008)
print(f'ID: {Movie.id_counter}. {mib.title} was released in the year {mib.year}')


print()