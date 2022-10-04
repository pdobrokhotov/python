'''
The open() function returns an object representing the file. Here, open('pi_digits.txt')
returns an object representing pi_digits.txt. Python stores this object in
file_object, which we’ll work with later in the program.
------------------------------------------------------
You can open a file in read mode ('r'), write mode ('w'), append mode ('a'), 
or a mode that allows you to read and write to the file ('r+'). 
If you omit the mode argument, Python opens the file in read-only mode by default.
-------------------------------------------------------
'''
#=========================================================================================
print("====== Show file content ============") 
#The keyword with closes the file once access to it is no longer needed.  
#if file is not in current filder use: with open('text_files\filename.txt') as file_object:
with open('pi_digits.txt','r') as file_object:
    contents = file_object.read()
    print(contents.rstrip()) # make sure there are no blank lines in the end
    
'''  
======================= NOTES ==========================================
Notice how we call open() in this program but not close(). You could open
and close the file by calling open() and close(), but if a bug in your program
prevents the close() statement from being executed, the file may never
close. This may seem trivial, but improperly closed files can cause data
to be lost or corrupted. 
All you have to do is open the file and work with it as desired,
trusting that Python will close it automatically when the time is right.
=========================================================================
'''
#====================================================================
print("====== Show file content lin3 by line ============") 
filename = 'pi_digits.txt'
pi_string = ''
# WITH-clause lakes sure the file wil be closed properly !!
with open(filename) as file_object:
    file_rows = file_object.readlines() # save file lines in LIST
#----------------------------------------------
# By now the file is closed properly but its content 
# we have in variable = file_rows alredy!
for file_row in file_rows:
    pi_string += file_row.strip()
print(pi_string) # or print(pi_string[:10] + "...") if want less digits on screen
print(len(pi_string))

'''  Chck if your birsfay inside pi
birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
   print("Your birthday appears in the first million digits of pi!")
else:
   print("Your birthday does not appear in the first million digits of pi.")
 ===================== use replace if needed ======================
 message.replace('dog', 'cat')
 
'''