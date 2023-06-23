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
Create object, one_obj for the class who can access all the attributes of the class Employee.
Process of object creation is also known as object instantiation
'''

one_obj = Employees()
# print(f"GPN is {one_obj.gpn}")
# print(f"First Name is {one_obj.f_name}")
# print(f"Last Name is {one_obj.l_name}")

print(one_obj.displayRecords())

print("----------------------------------------------------------EOL----------------------------------------------------------")

class Sales():
    f_name = "Ben"
    l_name = "Stokes"
    sales = 10
    def hasAchivedSales(self):
        if self.sales >= 10:
            print("Targeted Sales has been achived")
        else:
            print("Targeted Sales has been missed")
            
obj_two = Sales()
print(obj_two.hasAchivedSales())