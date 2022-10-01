bicycles = ['trek', 'cannondale', 'redline', 'specialized']
bicycles = ["trek", "cannondale", "redline", "specialized"]
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
#=======================================================================================
print("===================================================================")

#=======================================================================================
#=======================================================================================
print("===================================================================")