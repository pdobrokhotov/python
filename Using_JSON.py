import json
'''
The json module allows you to dump simple Python data structures into a
file and load the data from that file the next time the program runs. You can
also use json to share data between different Python programs. Even better,
the JSON data format is not specific to Python, so you can share data you
store in the JSON format with people who work in many other programming
languages. It’s a useful and portable format, and it’s easy to learn.
-----------------------------------------------------------------------------------------
Note The JSON (JavaScript Object Notation) format was originally developed for JavaScript.
However, it has since become a common format used by many languages, including Python.
'''

#=====================================================================================
print("\n====== Dump data to file using JSON ============\n") 
numbers = [2, 3, 5, 7, 11, 13]
filename = 'numbers.json'
# As a resut of code below we see string = [2, 3, 5, 7, 11, 13] in file 'numbers.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)
#=====================================================================================
print("\n====== Load data from file using JSON ============\n") 
filename = 'numbers.json'
with open(filename) as f_obj:
    numbers = json.load(f_obj)
print(numbers)
# We can also print each number, taken from file, separately
for each_nun in numbers:
    print(each_nun)
    

#=====================================================================================
print("\n====== Read data from user input using JSON. If no file, create it ============\n") 
filename = "" # or instead of empty string we could use: filename = None 
try:
    with open(filename) as f_obj:
        username = json.load(f_obj)
except FileNotFoundError:
    username = input("What is your name? ")
    if username: # if username = "" or None, this lines = False
        filename = username + '.json'
    else:
        filename = "username.json"   
        #return None   #here we could also use RETURN-statement     
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
        print("We'll remember you when you come back, " + username + "!")    
else:
    print("Welcome back, " + username + "!")    
