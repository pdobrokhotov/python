#=========================================================================
#============= FUNCTION THAT WQRK LIKE PROCEDURE  ======================== 
print("=================== procedure-like function =======================")
#=================================================================================
def describe_pet(animal_type, pet_name='unknown'): # "def" means function definition
    """Display information about a pet.""" # this is doc-string that uses trple quotes
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
#--------------------- call function ---------------------------------
describe_pet('harry', 'hamster')
# or using named params
describe_pet(animal_type='hamster', pet_name='harry')
# launcg using defauls
describe_pet(animal_type='dog')

#=========================================================================
#============= FUNCTION RETURNINF VALuE ================================== 
print("========= function returning value =================================")

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
#-------------------- cal function ---------------------
musician = get_formatted_name('jimi', 'hendrix')
print(musician)
musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)
#========================================================================

def build_person(first_name, last_name, age=''):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person
#----------------------------------------------------------------
musician = build_person('jimi', 'hendrix', age=27)
print(musician)

#=========================================================================
#============= FUNCTION WITH VARYING NUMBER OF ARGUMENTS ================= 
# NOTE: If you want a function to accept several different kinds of arguments, 
# the parameter that accepts an arbitrary number of arguments must be placed
# last in the function definition, like: def make_pizza(size, *toppings):
print("========= function wuth varying number of args ====================")
#asterisk in the parameter name *toppings tells Python to make an empty tuple called toppings
def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    #print(toppings) # = ('mushrooms', 'green peppers', 'extra cheese')
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)
#---------------- call function --------------------------
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')


#=========================================================================
#============= FUNCTION WITH VARYING NUMBER OF KEY-VALUES PAIRS ==========
# NOTE: If you want a function to accept several different kinds of arguments, 
# the parameter that accepts an arbitrary number of arguments must be placed
# last in the function definition, like: def make_pizza(size, **toppings):
print("========= function wuth varying number of args ====================")
# Double asterisk (**) in the parameter name **toppings tells Python 
# to make an empty Dictionary called toppings
#========================================================================
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    # Return result
    return profile
#---------------------- call function -------------------
user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')
print(user_profile)
#-------------- call function-------------------
user_profile = build_profile('albert', 'einstein',
location='princeton',
field='physics')
print(user_profile)