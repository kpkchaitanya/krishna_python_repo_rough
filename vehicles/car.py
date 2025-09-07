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