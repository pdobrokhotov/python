'''
The try-except-else block works like this: Python attempts to run the
code in the try statement. The only code that should go in a try statement
is code that might cause an exception to be raised. Sometimes you have
additional code that should run only if the try block was successful; 
This code goes in the else block. The except block tells Python what to do in case
a certain exception arises when it tries to run the code in the try statement.
'''
#=================================================================
print("====== Catching exceptions: division by 0 ============") 
try:
    a = 5
    b = 1   
    answer = a/b
    #answer+= "Result = "
except ZeroDivisionError:
    print("You can't divide by zero!")
except TypeError:
    print("You tried to concatenate string with number")
else:
    print(answer)
#=================================================================

filename = 'alice.txt'
try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)
    