
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