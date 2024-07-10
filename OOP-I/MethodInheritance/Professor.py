class Professor:

    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course


    def greet_students(self):
        print("Welcome to the class")


class ScienceProfessor(Professor):

    def greet_students(self):
        print("Hi everyone!. It's a great day to study science!")
        Professor.greet_students(self)


physics = ScienceProfessor("Tesla", 45, "Electrical Engineering")
print(physics.greet_students())
