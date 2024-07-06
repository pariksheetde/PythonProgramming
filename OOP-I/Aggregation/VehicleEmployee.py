class Vehicle:

    def __init__(self, brand, color, reg_id, is_electric):
        """This function acts as a constructor with 4 instance attributes"""
        self.brand = brand
        self.color = color
        self.reg_id = reg_id
        self.is_electric = is_electric

    def show_reg_id(self):
        """This function is used to return registration id of the vehicle"""
        return self.reg_id
    
    def show_info(self):
        """This function defined inside Vehicle class will be called by instance of Employee"""
        print(f"My Vehicle Info.....")
        print(f"Color: {self.color}")
        print(f"Registration ID: {self.reg_id}")
        print(f"Electric: {self.is_electric}")


class Employee:

    def __init__(self, name, vehicle):
        """This function acts as a constructor with 2 instance attributes"""
        self.name = name
        self.vehicle = vehicle

    def show_vehicle_info(self):
        """This function is used to refer vehicle instance inside employees class"""
        return self.vehicle.show_info()

bmw = Vehicle(brand='BMW', color='Black', reg_id='AZ-1567', is_electric=False)
dep = Employee('Pariksheet', bmw)

print(dep.show_vehicle_info())
print(f'I own {dep.vehicle.brand}. Color: {dep.vehicle.color}. Reg ID: {dep.vehicle.reg_id}')

print()

print(f'Registration ID: {dep.vehicle.show_reg_id()}')

print()