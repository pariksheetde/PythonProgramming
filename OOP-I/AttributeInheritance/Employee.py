class Employee:

    def __init__(self, full_name, salary):
        self.full_name = full_name
        self.salary = salary

class Programmer(Employee):

    def __init__(self, full_name, salary, programming_language):
        Employee.__init__(self, full_name, salary)
        self.programming_language = programming_language


pariksheet = Programmer("Pariksheet De", 10000, ['SQL', 'Python'])
print(f'{pariksheet.full_name} skill sets are {pariksheet.programming_language}. He earns approximately {pariksheet.salary}')