#A dictionary in Python is a collection of key-value pairs. Each key is connected
#to a value, and you can use a key to access the value associated with that key.
#A key’s value can be a number, a string, a list, or even another dictionary.
#In fact, you can use any object that you can create in Python as a value in a dictionary.
#=========================================================================================
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])  # = green
print(alien_0['points']) # = 5
#add new key-value pairs to dictionary above
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0) # = {'color': 'green', 'points': 5, 'x_position': 0, 'y_position': 25}
#NOTE: the order of the key-value pairs may not match the order in which we add them
#      Python doesn’t care about the order in which you store each key-value pair; 
#      it cares only about the connection between each key and its value.
#======================================================================================
print("===============================================================================")
#We can start with empty dictiuonary nad add value later
alien_0 = {}
alien_0['color'] = 'red'
alien_0['points'] = 77
print(alien_0) # = {'color': 'red', 'points': 77}
# we can modify existing value for a given key
alien_0['color'] = 'yellow'
print(alien_0) # = {'color': 'yellow', 'points': 77}
#======================================================================================
print("========================= Removing Key-Value Pairs =======================================")
#removong value from Dictionary resembles the way it's done with LISTS
alien_0 = {'color': 'green', 'points': 5}
print(alien_0) # = {'color': 'green', 'points': 5}
del alien_0['points'] # remove value (=5) by KEY = 'points'
print(alien_0) # = {'color': 'green'}
#========================================================================
print("========================= Looping Dictionary using Items() =======================================")
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
print("Sarah's favorite language is " 
    + favorite_languages['sarah'].title() 
    + "."
    )
# Check if a given key = 'erin' exists among Dictionary's keys. Because the keys() method 
# isn’t just for looping: It actually returns a list of all the keys
if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

# We can loop only keys using = .items() , that has both key and value
for key, value in favorite_languages.items():
    print("\nKey: " + key)
    print("Value: " + value)
#========================================================================
print("========================= Looping Dictionary using Keys() =======================================")
# We can loop only keys using = .keys() that has only key
for name in favorite_languages.keys():
    print(name.title() )
# Keys are default. Thus "for name in favorite_languages:" will produce the same effect as above
#========================================================================
print("========================= Looping Dictionary using Values() =======================================")
# We can loop only keys using = .values() that has only key
for language in favorite_languages.values():
    print("Current value = " + language.title() )

#========================================================================    
print("========================= Check Dictionary by LIST =======================================")
friends = ['phil', 'sarah']
# We start looping our dictionary's keys (by sorting it first) 
# and for current key check if it exists in our LIST
for name in sorted(favorite_languages.keys()):
    #print(name.title())
    if name in friends:
        print(" Hi " + name.title() + ", I see your favorite language is " +
        favorite_languages[name].title() + "!")

#=================================================================
#===================== UNIQUE LISTS ==============================
#=================================================================
#To get unique list of values either for Dictionaries or Lists we use SET()-function
# SET-function removes duplicates! 
print("============= GET UNIQUE LIST using SET()-function ===============================")
friends = ['zak','zak','zak', 'fill', 'fill','dave','arnold','arnold','arnold','arnold']
print(friends)      # = ['zak', 'zak', 'zak', 'fill', 'fill', 'dave', 'arnold', 'arnold', 'arnold', 'arnold']
print(set(friends)) # = {'zak', 'dave', 'arnold', 'fill'} 

#=================================================================
#===================== NESTING DICTIONARIES ====================== 
#=================================================================
#We can have Dictionary of dictionaries 
print("============= Dictionary of dictionaries  ===============================")
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens_all = [alien_0, alien_1, alien_2]
for current_alien in aliens_all:
    print(current_alien)
################################################################
#A more realistic example would involve more than three aliens with
#code that automatically generates each alien. In the following example we
#use range() to create a fleet of 30 aliens:
################################################################
print("=============  more realistic example  ===============================")
# Make an empty list for storing aliens.
aliens = []
print (range(10)) # = range(0, 10)
# Make 30 green aliens.
for alien_number in range(10): # range() returns a set of numbers
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
    
# Show the first 5 aliens:
for alien in aliens[:5]: # print only the first 5 items among 10
    print(alien)
print("...")

# Show how many aliens have been created.
print("Total number of aliens: " + str(len(aliens))) # = 10 items
################################################################
#=== Update a dictionary element in the DICTIONARY of dictionaries =========
print("=============  more realistic example (advanced)  ===============================")
for alien in aliens[0:3]:
    if alien['color'] == 'green':
       alien['color'] = 'yellow'
       alien['speed'] = 'medium'
       alien['points'] = 10
# Show the first 5 aliens: (index = 0,1,2,3,4)
for alien in aliens[:5]:
    print(alien)

################################################################
#================== A List in a Dictionary =====================
# We can keep a list object as a value for a given KEY in dictionary
print("=============  A List in a Dictionary ===============================")
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
    }
# Summarize the order.
print("You ordered a " + pizza['crust'] + "-crust pizza " + "with the following toppings:")
for topping in pizza['toppings']:
    print("\t" + topping)
    
 ################################################################
#================== A List in a Dictionary (advanced) =========== 
# We can keep a list object as a value for a given KEY in dictionary
# In this case we use nested loops
print("=============  A List in a Dictionary(advanced) ======================")   
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],     
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
    }
for name, languages in favorite_languages.items():
    print("\n" + name.title() + "'s favorite languages are:")
    for language in languages:
        print("\t" + language.title())   
    
################################################################
#========== A child dictionary in a parent Dictionary ========== 
# We can keep a list object as a value for a given KEY in dictionary
# In this case we use nested loops
print("====== A child dictionary in a parent Dictionary ============")       
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        },
}
#-----------------------------------------------------------------------
for username, user_info in users.items():
    print("Username: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']
    print("Full name: " + full_name.title() + "; " +  "Location: " + location.title() +"\n")
    
################################################################
#========== Filling a Dictionary with User Input ========== 
# We can keep a list object as a value for a given KEY in dictionary
# In this case we use nested loops
print("====== Filling a Dictionary with User Input ============")      
responses = {}
# Set a flag to indicate that polling is active.
polling_active = True
while polling_active:
    # Prompt for the person's name and response.
    name = input("\nWhat is your name? ")
    response = input("What is your age? ")
    # Store the response in the dictionary:
    responses[name] = response
    # Find out if anyone else is going to take the poll.
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
       polling_active = False
    # Polling is complete. Show the results.
       print("\n--- Poll Results ---")
       
for name, response in responses.items():
    print(name + " has age of " + response + ".")
  