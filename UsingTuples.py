#=======================================================================================
#====================== USUNG TUPLES (I.E LISTS THAT CANNOT BE EDIT)==================== 
#=======================================================================================
# Defining a Tuple. A tuple looks just like a list except you use parentheses instead 
# of square brackets. Once you define a tuple, you can access individual elements 
# by using each item’s index, just as you would for a list.
# For example, if we have a rectangle that should always be a certain size,
# we can ensure that its size doesn’t change by putting the dimensions into a tuple
# When compared with lists, tuples are simple data structures. Use them when you want 
# to store a set of values that should not be changed throughout the life of a program.
print("===================================================================")
dimensions = (200, 50) # two elemets in our tuple, that is by fact IMMUTABLE LIST
print(dimensions)      # = (200, 50)
print(dimensions[0])   # = 200
print(dimensions[1])   # = 50

# Modifying tuple will give error! = 'tuple' object does not support item assignment
# dimensions[0] = 250

#=======================================================================================
#Though we can change tuple we can REDIFINE it
dimensions = (400, 100)
print(dimensions)
dimensions = (10, 20)
print(dimensions)

#=======================================================================================
print("================ LOOPING TUPLE IS THE SAME LIKE LOOPING LIST=====================")
for dimension in dimensions: 
    print(dimension)


#=======================================================================================
print("======================================================================")
#=======================================================================================
print("======================================================================")
#=======================================================================================
print("======================================================================")
#=======================================================================================
print("======================================================================")

