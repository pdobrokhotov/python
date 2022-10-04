#============================== ATTENTION ==================================================
#If you specify a default value for a parameter, no spaces should be used on either side of the equal sign:
# def function_name(parameter_0, parameter_1='default value')
#===========================================================================================
def describe_pet(animal_type, pet_name='unknown'): # "def" means function definition
    """Display information about a pet.""" # this is doc-string that uses trple quotes
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

#=========================================================================
def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name: # Python interprets non-empty strings as True,
       full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
       full_name = first_name + ' ' + last_name
    #return resulted value  
    return full_name.title()
    #instead of returning string we could return dictionary as shown below
    #person = {'first': first_name, 'last': last_name}
    #return person
#========================================================================

def build_person(first_name, last_name, age=''):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

#=========================================================================
def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    #print(toppings) # = ('mushrooms', 'green peppers', 'extra cheese')
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

#=========================================================================
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    # Return result
    return profile
#=========================================================================
