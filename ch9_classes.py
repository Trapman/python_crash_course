# creating and using a class###
class Dog:
    """This attempts to model a dog"""
    
    def __init__(self, name, age):
        """initialize name and age attributes"""
        self.name = name
        self.age = age
        
    def sit(self):
        """simulate a dog sitting in response to a command"""
        print(f"{self.name} is now sitting.")
        
    def roll_over(self):
        """simulate a dog rolling over in response to a command"""
        print(f"{self.name} rolled over!")

#############
# making an instance from a class
# basically the class is a set of instructions for how to make an instance

my_dog = Dog('Henley', 5)
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

# accessing attributes
my_dog.name
my_dog.age

# calling methods
my_dog.sit()
my_dog.roll_over()

# creating multiple instances
my_dog = Dog('Henley', 5)
savuol_dog = Dog('Buford', 6)

print(f"My dog's name is {my_dog.name}.")
print(f"Savuol's dog's name is {savuol_dog.name}")

print(f"n\My dog is {my_dog.age} years old.")
your_dog.sit
##############
class Restaurant:
    """This builds a restaurant"""
    
    def __init__(self, restaurant_name, cuisine_type):
        """initializes name and type attributes"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        
    def describe_restaurant(self):
        """describes the name and type of a restaurant"""
        print(f"The restaurant's name is {self.restaurant_name} and it offers {self.cuisine_type} cuisine.")
        
    def open_restaurant(self):
        "tells whether the restaurant is open"
        print(f"{self.restaurant_name} is open.")
        
# Working with classes and instances
"""once you create a class, you'll spend most of your time working with instances 
from that class. One of the first tasks you'll want to do is modify the attributes
associated with those instances. You can modify them directly or use methods to upate them."""

#The Car Class
"""class represents a car, stores info about what kind of car, and has a method
that will summarize this info"""
class Car:
    """A simple attempt to represent a car."""
    
    def __init__(self, make, model, year):
        """initializes attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
my_new_car = Car('tesla', 's100', 2022)
print(my_new_car.get_descriptive_name())

#Setting a default value for an attribute
"""we'll add an odometer_reading value and set it to 0"""
self.odemeter_reading = 0

def read_odometer(self):
    """Print a statement to show the car's mileage."""
    print(f"This car has {self.odometer_reading} miles on it.")
#######################################################

#modifying attribute values: 3 ways to do this

#(1) Access the attribute directly through the instance
my_new_car.odometer_reading = 23
my_new_car.read_odometer()
# all we did here was directly change the odometer reading from 0 to 23

#(2) Modify attribute through a method
def update_odometer(self, mileage):
    """set the odometer reading to the given value."""
    self.odometer_reading = mileage
    
my_new_car.update_odometer(23)
my_new_car.read_odometer()

# bonus: adding logic to keep someone from rolling back mileage on odometer
def update_odometer(self, mileage):
    """
    set the odometer reading to the given value.
    Reject the change if it attempts to roll the odometer back.
    """
    if mileage >= self.odometer_reading:
        self.odometer_reading = mileage
    else:
        print("You can't roll back an odometer!")
    self.odometer_reading = mileage
    
#(3) Incrementing an Attribute's value through a method
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles
        
my_used_car = Car('buick', 'roadmaster', 1996)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()
    
class Car:
    """A simple attempt to represent a car."""
    
    def __init__(self, make, model, year):
        """initializes attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0   #Setting a default value for an attribute
        
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def update_odometer(self, mileage):
        """
        set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
            self.odometer_reading = mileage

    def read_odometer(self):
        """Print a statement to show the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")
        
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles
    
my_used_car = Car('buick', 'roadmaster', 1996)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()
#################################
