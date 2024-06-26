class Movies:
    def __init__(self, title, rating, year):
        self.title = title
        self._rating = rating
        self.year = year
    
    def get_rating(self):
        return self._rating
    
    def set_rating(self, new_rating):
        """This method is used to modify the value of the object"""
        if new_rating >= 9 and isinstance(new_rating, float):
            self._rating = new_rating
        else:
            print("Enter the rating greater than 9")
            self._rating = new_rating


Godfather = Movies("The Godfather Part 1", 9.2, 1972)
print(f'I loved "{Godfather.title}". Rating was {Godfather.get_rating()}, Yeh I know it was released in the year {Godfather.year}')

print()

titanic = Movies("Titanic", 7, 1997)
print(f'I loved "{titanic.title}". Rating was {titanic.get_rating()}. But somehow the rating is not correct')

print("Titanic movie rating was not correct, it's per below the actual so need to update the rating \
Let's update the rating")
titanic.set_rating(1)
print(f'New rating for {titanic.title}: {titanic.get_rating()}')

print()
