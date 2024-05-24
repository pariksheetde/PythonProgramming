
class Sales():
    f_name = "Ben"
    l_name = "Stokes"
    sales = 10
    def hasAchivedSales(self):
        if self.sales >= 10:
            print("Targeted Sales has been achived")
        else:
            print("Targeted Sales has been missed")
            
'''        
Create object, obj_two for the class who can access all the attributes of the class Sales.
Process of object creation is also known as object instantiation
'''
            
obj_two = Sales()
print(obj_two.hasAchivedSales())