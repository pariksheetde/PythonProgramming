class Employees():
    gpn = 100
    f_name = "Pariksheet"
    l_name = "De"
    def displayRecords(self):
        if self.gpn == 100:
            print(f"Employee is {self.f_name}")
        else:
            print(f"Might be some other employee")
        return

'''        
create object, one_obj for the class who can access all the attributes of the class Employee.
process of object creation is also known as object instantiation
'''

one_obj = Employees()
# print(f"GPN is {one_obj.gpn}")
# print(f"First Name is {one_obj.f_name}")
# print(f"Last Name is {one_obj.l_name}")

print(one_obj.displayRecords())