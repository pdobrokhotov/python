#=======================================================================================
#=====================  Looping Through an Entire List =================================
print("===================================================================")
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

#=======================================================================================
#==========  Making Numerical Lists ====================================================
#=======================================================================================
print("===================================================================")
# Python’s range() function makes it easy to generate a series of numbers.
# Also function list() converts result of range() function into LIST
numbers = list(range(1,6)) #strangely enough, but the list is [1, 2, 3, 4, 5] excluding last number = 5
print (numbers)
for number in numbers:
    print(number)  
# range() function has a 3d parameter that acts as an increment value
even_numbers = list(range(2,11,2)) # the result is a list od even numbers = [2, 4, 6, 8, 10]
print(even_numbers) 
#=======================================================================================
print("===================================================================")
squares = []
for value in range(1,11):
 square = value**2
 squares.append(square)
print(squares) # = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#=======================================================================================
#------------------------- List Comprehensions -----------------------------------------
#======================== MORE ELEGANT CODE FOR LIST CREATION ========================== 
# A list comprehension allows you to generate this same list in just one line of code. A list comprehension combines the
# for loop and the creation of new elements into one line, and automatically appends each new element.
# The syntax below is called "List Comprehension", when we insert loop into list declaration
squares = [value**2 for value in range(1,11)] # = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print("===================================================================")

#=======================================================================================
#======================== Simple Statistics with a List of Numbers =====================
#Use functions : max, min, sum with LISTS
print("===================================================================")
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

#=======================================================================================
#====================== Working with Part of a List ==================================== 
print("===================================================================")
#Slicing list. ATTENTION! 
#Note that [0:3] means items = 0,1,2 and NOT 0,1,2,3. The "3"-element is ignored!
# NOTES: LISTS are zero based ans we can refer the 1st elemeet as bicycles[0]
#        Also we can refer to range like: bicycles[0:3] or bicycles[:3]
# But NOTE that the upper value = 3 means actualy 2. 
# I.e. [0:3] means 0,1,2 and [:3] means also 0,1,2 ("3" is NOT included)
# Also you may set range exluding the upper bound, like players[2:])
#---------------------------------------------------------------------------------------
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3]) # = ['charles', 'martina', 'michael'] (there's no "florence" here as oner could expect)
# Also we can omit 1st argument. It means start from the first item (index=0) 
# till the item with index = 3 (NOT 4!)
print(players[:4]) # = ['charles', 'martina', 'michael', 'florence']
print(players[2:]) # = ['michael', 'florence', 'eli']
#=======================================================================================
#Recall that a negative index returns an element a certain distance from the end of a list;
#therefore, you can output any slice from the end of a list. For example, if
#we want to output the last three players on the roster, we can use the slice = players[-3:]
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[-3:]) # ['michael', 'florence', 'eli']

#=======================================================================================
#=========================== Looping Through a Slice =================================== 
print("===================================================================")
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team:")
for player in players[:3]: # this range means ['charles', 'martina', 'michael']
    print(player.title())
#=======================================================================================
#========================== Copying a List ==============================================
print("===================================================================")
my_foods = ['pizza', 'falafel', 'carrot cake']
# when copying the list make sure you are copying the list using a slice! I.e. use [:] 
friend_foods = my_foods[:] 
#----------------------------IMPORTANT! ---------------------------------------------
# Note, that command above is NOT the same like  friend_foods = my_foods 
# Because if we use friend_foods = my_foods instead of friend_foods = my_foods[:] 
# our appendings will work to both LISTS, 'cause in fact we just created a new refernce 
# to the same lIST and thus both lists  "my_foods" and "friend_foods" will show the same
# because both variables point to the same list
#------------------------------------------------------------------------------------
# Now add elenets to both LISTS
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

#====================== USING IF-STATEMENT IN LOOP =====================================
print("===================================================================")
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
# Check if value is in the LIST

if 'audi' in cars:
    print ("audi is present in the LIST")
if 'mercedez' not in cars:
    print ("mercedez is NOT present in the LIST")

print ("asd" == "Asd") # = False 'cause string comparison is caption specific
#---------------------------------------------------------------------------
age = 12
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:    # Note that thi last elif-branch can be omited 
    print("Your admission cost is $5.")
elif age >= 100:  # Note that thi last elif-branch can be omited 
    print("Your admission cost is $77.")   
else:             # Note that thi last else-branch can be omited
    print("Your admission cost is $10.")
#---------------------------------------------------------------------------
#Check if list is empty
requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")

#=================================================================
#===================== SORTING LISTS =============================
#=================================================================
print("========================= LOOP SORTED LIST =======================================")
friends = ['zak', 'fill','dave','arnold']
# We start looping our dictionary's keys (by sorting it first) 
# and for current key check if it exists in our LIST
for name in sorted(friends):
    print(name)
#=================================================================
#===================== UNIQUE LISTS ==============================
#=================================================================
print("============= GET UNIQUE LIST using SET()-function ===============================")
friends = ['zak','zak','zak', 'fill', 'fill','dave','arnold','arnold','arnold','arnold']
print(friends) 
print(set(friends))    
   
#=======================================================================================
#=======================================================================================
print("================= LOOPING USING RANGE-function =====================================")
# Range starts at index = 0
for my_number in range(10): # loop 10 times
    print("my_number = " + str(my_number))
    
#=======================================================================================
#=======================================================================================
print("================= LOOPING USING WHILE =====================================")
current_number = 1
while current_number <= 5:
    print("current_number = " + str(current_number))      
    current_number += 1

#=======================================================================================
#======================= Moving Items from One List to Another ========================= 
print("================= Moving Items from One List to Another =========================")
# Start with users that need to be verified, and an empty list to hold confirmed users.
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
# Verify each user until there are no more unconfirmed users.
# Move each verified user into the list of confirmed users.
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)
# Display all confirmed users.
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
    

#=======================================================================================
#================ Removing All Instances of Specific Values from a List================= 
print("============ Removing All Instances of Specific Values from a List ==============")
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
   pets.remove('cat')
print(pets)