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

# basically 3 main ways of structuring arguments #########
# (1) Positional Arguments 
# when you call a function, python must match each argument in the func call with a parameter in the func defintion.
# the simplest way to do this is based on the order of the arguments
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
    
describe_pet('bulldog', 'henley')
describe_pet('cat', "halle")
# order matters in positional arguments

# (2) Keyword Argument
# you can also use this approach to avoid having to worry about order
describe_pet(animal_type='bulldog', pet_name='henley') # this is the main difference

# (3) Default Values
# basically you're hard-coding a default value for each parameter
def describe_pet(pet_name, animal_type = 'dog'):

describe_pet(pet_name = 'henley')

# because positional, keyword, and default values can all be used together, you'll often have several equivalent ways to call a function

# return values
"""a function doesn't always have to display its output directly, and instead can return a value or set of values
the value the function returns is called a return value. The return statement takes a value inside a funct
and sends it back to the line that called the function. Return values allow you to move much of your program's 
grunt work into functions"""
#returning a simple value
def get_formatted_name(first_name, last_name):
    """return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('maynard', 'keenan')
print(musician)

# making an argument optional
def get_formatted_name(first_name, last_name, middle_name=''):   # this makes the middle name optional
    """return a full name, neatly formatted."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('maynard', 'keenan', 'james')
print(musician)
# the optional value is listed last, and uses an empty string as a default value 

# returning a dict
def build_person(first_name, last_name):
    """Return a dict of info about a person"""
    person = {'first': first_name, 'last': last_name}
    return person

streamer = build_person('doctor', 'disrespect')
print(streamer)

# returning a more complex dict
def build_person(first_name, last_name, age=None):
    """Return a dict of info about a person"""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

streamer = build_person('doctor', 'disrespect', age=38)
print(streamer)

###########
