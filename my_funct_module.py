'''
This is good practice: a function should either return
the value you’re expecting, or it should return None
'''

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
#=========================================================================
#=========================================================================

def count_words(filename, ignore_error_flag = False):
    # Count the approximate number of words in a file. 
    # Run this function as shown below:
    #-------------------------------------------------------------------------------------
    # filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
    # for filename in filenames:
    #     count_words(filename) 
    #-------------------------------------------------------------------------------------  
    # Using the try-except block allows thus program to run withot error even if error occur 
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        if ignore_error_flag:
           pass  # instead of line below we could use "pass" command to ignore error silently
        else :
           print("Sorry, the file [" + filename + "] does not exist.")
    else:
        # Count approximate number of words in the file.
        # Note, that we could also use counting special word: line.lower().count('row')
        words = contents.split()
        num_words = len(words) 
        print("The file [" + filename + "] has about " + str(num_words) + " words.")

#========================================================================================
#=============== FUNCTION USED FOR TESTING in [TESTING_FUNCTION.py] ===================== 
#========================================================================================
def get_formatted_name(first, last, middle=''):
    """Generate a neatly formatted full name."""
    if middle:
        full_name = first + ' ' + middle + ' ' + last
    else:
        full_name = first + ' ' + last
    return full_name.title()
#========================================================================================
