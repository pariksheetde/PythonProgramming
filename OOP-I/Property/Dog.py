class Dog:
    def __init__(self, age):
        self._age = age

    def get_age(self):
        """This method is used to get the value of the object"""
        print("Calling the getter.....")
        return self._age

    def set_age(self, new_age):
        """This method is used to modify the value of the object"""
        print("Calling the setter.....")
        if isinstance(new_age, int) and (new_age > 0 and new_age <= 5):
            self._age = new_age
        else:
            print("Invalid age")

    # create accessor & mutator using property
    age = property(get_age, set_age)
    
puppy = Dog(7)
print(f'Puppy is {puppy.age} years old')

puppy.set_age(5)
print(f'Puppy is {puppy.age} years old')