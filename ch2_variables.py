message = 'Hello World!'
print(message)

# Changing Case in a String with Methods
name = 'david mega'
print(name.title())

name2 = 'chris lodise'
print(name2.upper())
print(name2.lower())

# Using Variables in Strings (this is called the f-string method)
first_name = 'heather'
last_name = 'ward'
full_name = f"{first_name} {last_name}"
print(full_name)

first_name = 'heather'
last_name = 'ward'
full_name = f"{first_name} {last_name}"
print(f"Hello, {full_name.title()}!")

first_name = 'heather'
last_name = 'ward'
full_name = f"{first_name} {last_name}"
message = f"Hello, {full_name.title()}!"
print(message)
"""basically the way this works is that you place the letter F immediately before the opening quotation mark. 
   Put braces around the name or names of any variables you want to us inside the string.
   Python will replace each variable with its value when the string is displayed"""
   
# Adding Whitespace to a String with Tabs (\t) or Newlines (\n)
print("\tMega")   # prints Mega with a tab
print("Teams:\nSixers\nEagles\nFlyers\nPhillies")    Prints each item on its own line
print("Teams:\n\tSixers\n\tEagles\n\tFlyers\n\tPhillies") Prints new line and tab

# Stripping Whitespace using rstrip() and lstrip()
favorite_city = 'philadelphia'
favorite_city.rstrip()  # removes all whitespace on the right end of the string. NOTE this removes it temporarily
favorite_city = favorite_city.rstrip()  # removes it permanently by renaming the variable with rstrip()

   


