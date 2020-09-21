# defining a function
def greet_user():
    """Display a simple greeting."""
    print("Hello!")
    
greet_user()

# passing info to a function: arguments and parameters
def greet_user(username):
    """Display a simple greeting."""
    print(f"Hello, {username.title()}!")
    
greet_user('Hoang')

# Positional Arguments #########
# when you call a function, python must match each argument in the func call with a parameter in the func defintion.
# the simplest way to do this is based on the order of the arguments
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
    
describe_pet('bulldog', 'henley')
describe_pet('cat', "halle")
# order matters in positional arguments

# Keyword Argument
# you can also use this approach to avoid having to worry about order
describe_pet(animal_type='bulldog', pet_name='henley') # this is the main difference

# Default Values
# basically you're hard-coding a default value for each parameter
def describe_pet(pet_name, animal_type = 'dog'):

describe_pet(pet_name='henley')

# Equivalent Function Calls
