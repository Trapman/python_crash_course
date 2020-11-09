# creating and using a class
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
####
