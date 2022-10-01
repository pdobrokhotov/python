message = "Hello Python world!"
#print(message)
name = "test lowecase" 
#print (name.title()) # = Test Lowecase  
#print (name.upper()) # = TEST LOWECASE
#print (name.lower()) # = test lowecase  
#print (name + " " + message) # = test lowecase Hello Python world!
#print("Languages:\nPython\nC\nJavaScript")  # adds nextline char
#print("\tPython\nMy next line") # adds tab first and then nextline char
#print("Languages:\n\tPython\n\tC\n\tJavaScript")
# ========= striping spaces: rstrip)_,lstrip(),strip() ===========
msg = "mys string ending with space and tab \t" 
print (msg+ "suffix")
print (msg.rstrip()  + "suffix")

age = 23
message = "Happy " + str(age) + "rd Birthday!" # use str() function to conver into to string
print(message)