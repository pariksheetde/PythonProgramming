class Vehicle:

    def __init__(self, color, speed, fuel_type):
        self.color = color
        self.speed = speed
        self.fuel_type = fuel_type

class Car(Vehicle):

    def __init__(self, color, fuel_type, num_doors, is_electric=False, speed=60):
        Vehicle.__init__(self,color, speed, fuel_type)
        self.num_doors = num_doors
        self.is_electric = is_electric

bmw = Car("White", "Petrol", 4, is_electric=False, speed=200)
print(f'I have {bmw.color} which runs on {bmw.fuel_type}. It has {bmw.num_doors} and top speed is {bmw.speed}')