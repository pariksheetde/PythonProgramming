class Movie:
    def __init__(self, title, year, language, rating) -> None:
        self.title = title
        self.year = year
        self.language = language
        self.rating = rating

titanic = Movie("Titanic", 1997, "English", 8.7)
print(f'{titanic.title} was released in the year {titanic.year} in {titanic.language} and rating was {titanic.rating}')

jurassic_park = Movie("Jurassic Park", 1993, "English", 8.7)
print(f'{jurassic_park.title} was released in the year {jurassic_park.year} in {jurassic_park.language} and rating was {jurassic_park.rating}')

print()

