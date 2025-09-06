# bikes = ['trek', 'redline', 'giant']
# print(bikes)

# # squares = []
# # for x in range(1, 11):
# #     squares.append(x**2)

# squares = [x**2 for x in range(1, 11)]
# print(squares)

# # name = input('What is your name?')
# # print('Your name is '+name)

def greet_user():
    """Display a simple message"""
    print('greet_user function greets hello')

greet_user()


class Car:
    """A simple attempt to represent a car."""
    
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year

        # Fuel capacity and level in gallons
        self.fuel_capacity = 15.0
        self.fuel_level = 0.0

    def fill_gas_tank(self):
        """Fill the gas tank to capacity."""
        self.fuel_level = self.fuel_capacity
        print("Gas tank is now full.")

    def drive(self, distance): 
        """Simulate driving the car a certain distance."""
        fuel_needed = distance / 25.0  # Assuming 25 miles per gallon
        if fuel_needed <= self.fuel_level:
            self.fuel_level -= fuel_needed
            print(f"Drove {distance} miles.")
        else:
            print("Not enough fuel to drive the desired distance.")


    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.fill_gas_tank()
my_new_car.drive(100)
print(f"Fuel level: {my_new_car.fuel_level} gallons")# import unittest

# Create a new module for Car. Create multiple cars and import them and create a fleet of cars.
# Then test the fleet of cars.
