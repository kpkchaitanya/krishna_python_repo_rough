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


from vehicles.car import Car    

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.fill_gas_tank()
my_new_car.drive(100)
print(f"Fuel level: {my_new_car.fuel_level} gallons")# import unittest

# Create a new module for Car. 
# Create multiple cars and import them and create a fleet of cars.
# Then test the fleet of cars.
# THen Immediately move to Autogen & Langchain & Langgraphs
# Explore Data Structures
# Explore Flask APIs
# Explore Deployment
# Explore WebDevelopment / Django / Deployment
# Explore Data Science


