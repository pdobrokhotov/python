'''
You can open a file in read mode ('r'), write mode ('w'), append mode ('a'), 
or a mode that allows you to read and write to the file ('r+'). 
If you omit the mode argument, Python opens the file in read-only mode by default.
'''

print("====== Writing to EMPTY file ============") 
filename = 'file_to_write_in.txt'
with open(filename, 'w') as file_object: # open the file in write mode.
     file_object.write("\t\tSTART")  
     file_object.write("\nI love programming.") 
     file_object.write("\nI love creating new games.")  
     file_object.write("\n\t\tEND")  
print("====== Appent to EXISTING file ============")      
with open(filename, 'a') as file_object:
    file_object.write("\nI also love finding meaning in large datasets.")
    file_object.write("\nI love creating apps that can run in a browser.\n")
   
''' 
#=====================================================================================   
# Write data using JSON LIBRARY    
#=====================================================================================   
import json    
#=====================================================================================
print("\n====== Dump data to file using JSON ============\n") 
numbers = [2, 3, 5, 7, 11, 13]
filename = 'numbers.json'
# As a resut of code below we see string = [2, 3, 5, 7, 11, 13] in file 'numbers.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)
#=====================================================================================
'''  