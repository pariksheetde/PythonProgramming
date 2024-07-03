class Flight:

    max_passenger = 3

    def __init__(self, number):
        self.number = number
        self.passengers = []
        self.waiting_list = []

    def add_passenger(self, passenger_list):
        if len(self.passengers) >= Flight.max_passenger:
            self.waiting_list.append(passenger_list)
        else:
            self.passengers.append(passenger_list)

# STEP 1. Create a instance of class
quantas = Flight("NI09")

# STEP 2. add a passenger to the add_passenger() of instance
quantas.add_passenger("Monica")
print(quantas.passengers)

quantas.add_passenger("Kate")
print(quantas.passengers)

quantas.add_passenger("Peter")
print(quantas.passengers)

quantas.add_passenger("Alex")
print(f'{quantas.passengers} have been added to the flight')
print(f'{quantas.waiting_list} is added in the waiting list')

print()
