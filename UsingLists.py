bicycles = ["trek", "cannondale", "redline", "specialized"]
# NOTES: LISTS are zero based ans we can refer the 1st elemeet as bicycles[0]
#        Also we can refer to range like: bicycles[0:3] or bicycles[:3]
# But NOTE that the upper value = 3 means actualy 2. 
# I.e. [0:3] means 0,1,2 and [:3] means also 0,1,2 ("3" is NOT included)
# Also you may set range exluding the upper bound, like players[2:])
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(bicycles)
print(bicycles[0].upper()) # tale the 1st element = TREK
print(bicycles[-1]) # take the last element = specialized
print(bicycles[-2]) # take the previous to the last element = redline

bicycles[-1] = "new last value"
print(bicycles) 
#==============================================
#Appending Elements to the End of a List
bicycles.append('new appended value to the end')
print(bicycles) 
#Appending Elements to empty list
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)
#Inserting Elements into a List
motorcycles.insert(0, 'inserted value at index = 0')
print(motorcycles)
#deleting value from list
del motorcycles[0]
motorcycles[0]
print(motorcycles)
#=========================================================================
print("===================================================================")
# remove the last item by poping it out of list BUT STILL saving it in variable
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop() # 'suzuki' will be pushued out of the list
print(popped_motorcycle) # =  'suzuki'
print(motorcycles)       # = ['honda', 'yamaha']
print("===================================================================")
# remove  item at any position by poping it out of list BUT STILL saving it in variable
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop(0)
print(popped_motorcycle) # = honda

#==================== Removing an Item by Value================================
print("===================================================================")
motorcycles = ['honda', 'yamaha', 'suzuki']
print (motorcycles)
removed_item_value = 'yamaha'
motorcycles.remove(removed_item_value) # = ['honda', 'suzuki']
print(motorcycles)
print(removed_item_value)
#The remove() method deletes only the first occurrence of the value you specify. If there’s
#a possibility the value appears more than once in the list, you’ll need to use a loop to
#determine if all occurrences of the value have been removed.
#Remove-method DOES NOT allow to save value like pop()-method
#Thus before using it, save the removed value in variable first and then pass this variable to remove-method
#=======================================================================================
#===================== Sorting a List Permanently with the sort() Method ===============
print("===================================================================")
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)
#=======================================================================================
#================= Sorting a List Temporarily with the sorted() Function ===============
print("===================================================================")
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)
# --------------- Printing a List in Reverse Order -------------------------
print("===================================================================")
cars.reverse() # reverse order . this is permanent
# IT IS NOT the same like cars.sort(reverse=True)
# Notice that reverse() doesn’t sort backward alphabetically; 
# it simply reverses the current order of the list:
print("Print CARS in REVERSE ORDER")
print(cars)
# print the length of the LIST
print ("The length of the LIST is  = " + str(len(cars)) )

#=======================================================================================
#==========  Making Numerical Lists ====================================================
#=======================================================================================
print("===================================================================")
# Python’s range() function makes it easy to generate a series of numbers.
for value in range(1,10):
    print(value)

print("===================================================================")


#==================== Check LIST for values or ENPTY ========================
#---------------------------------------------------------------------------
#Check if list is empty. When the name of a list is used in an if statement, 
# Python returns True if the list contains at least one item; 
# An empty list evaluates to False
requested_toppings = []
#The comnparison to True or False will not work!
print(requested_toppings == True)  # = False
print(requested_toppings == False) # = false
#But the code below WORKS
if requested_toppings:
   print("List is FULL")
else:
   print("List is EMPTY")

#-------------------------------------------------------------------------------
 
if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")
#--------------------------------------------------------------------------
#Check if list  hav valie of
requested_toppings.append("a")
requested_toppings.append("b")
requested_toppings.append("c")

requested_toppings.remove('a') # delete by value 
del requested_toppings[0]      # delete by index
#print(requested_toppings)
if "a" in requested_toppings:
    print("'a' is present")
elif "b" in requested_toppings:
    print("'b' is present")
elif "c" in requested_toppings:
    print("'c' is present")    
else:
    print("this char is not precent")

#=================================================================
#===================== SORTING LISTS =============================
#=================================================================
print("========================= SORT LIST =======================================")
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