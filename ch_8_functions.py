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

# using a function with a while loop
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")
    
    f_name = input("First name: ")
    if f_name == 'q':
        break
    
    l_name = input("Last name: ")
    if l_name == 'q':
        break
    
    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")
    
# city names
def get_city_country(city, country):
    """Returns the name of a city and its country"""
    city_country_pair = f"{city}, {country}"
    return city_country_pair.title()

while True:
    print("\nPlease type the name of the city and the country of interest:")
    print("\nenter 'q' at any time to quit)")
    
    city_name = input("City name: ")
    if city_name == 'q':
        break
    
    country_name = input("Country name: ")
    if country_name == 'q':
        break
    
    city_country= get_city_country(city_name, country_name)
    print(f"\nThe city-country pair is {city_country}")
    
# make album
def make_album(artist_name, album_name, tracks = None):
    """builds a dict describing a music album with artist name and album name, optional track number"""
    album = {'artist': artist_name.title(), 'album': album_name.title()}
    if tracks:
        album['tracks'] = tracks
    return album
    
album1 = make_album("tool", "lateralus", 14)
print(album1)

def make_album2(artist_name, album_name, tracks = None):
    """builds a dict describing a music album with artist name and album name, optional track number
    uses a while loop and user input"""
    album = 
    
    
# passing a list into a function #########################################
def greet_users(names):
    """print a simple greeting to each user in the list."""
    for name in names:
        message = f"Hello, {name.title()}!"
        print(message)
        
usernames = ['trap', 'mega', 'hoang', 'vince']
greet_users(usernames)

# modifying a list in a function ############################################
#start with some designs that need to be 3D-printed
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

# simulate each design until none are left
# move each design to completed_models after printing
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)
    
# display all completed models
print("\nThe following models have been printed: ")
for completed_model in completed_models:
    print(completed_model)

# function version
def print_models(unprinted_designs, completed_models):
    """
    simulate printing each design, until none are left.
    move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)
        
def show_completed_models(completed_models):
    """show all the models that were printed"""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)
        
unprinted_designs = ['phone case', 'travis scott jordans', 'earthbound original']
completed_models = []

print_models(unprinted_designs, completed_models)  #print_models(unprinted_designs[:], completed_models) if you want a copy
show_completed_models(completed_models)

#note that if you want to prevent a function from modifying a list, use the slice notation [:]
"""function_name(list_name[:])""" # this is the syntax
# the slice notation makes a copy of the list to send to the function, so it doesn't modify it

####
