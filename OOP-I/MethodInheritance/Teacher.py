class Teacher:

    def __init__(self, full_name, id):
        self.full_name = full_name
        self.id = id

    def greetings(self):
        return(f"Welcome to my class. I am your teacher. My name is {self.full_name}")

class ScienceTeacher(Teacher):

    def __init__(self, full_name, id, subject):
        Teacher.__init__(self, full_name, id)
        self.subject = subject

    def greetings(self):
        # print(f'Calling Superclass\'s \'greeting()\': {Teacher.greetings(self)}')
        print(f'Calling Superclass\'s \'greeting()\': {super().greetings()}')
        return(f"I am your science teacher. Science is amazing. My name is {self.full_name}")
        

print()
print("Let's display Science Teacher's Biodata")
albert = ScienceTeacher("Albert Einstein", "AE101", ["Physics", "Chemistry"])
print(f"ID: {albert.id}. {albert.full_name} teaches {albert.subject}.")
print(f'{albert.greetings()}')

print()

print("Let's display Teacher's Biodata")
teacher = Teacher("Albert Einstein", "AE101")
print(f"ID: {teacher.id}. {teacher.full_name}.")
print(f'{teacher.greetings()}')

print()
