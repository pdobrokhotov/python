prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "
name = input(prompt)
print("\nHello, " + name + "!")

#=======================================================================================
#=======================================================================================
print("================= LOOPING USING WHILE =====================================")
current_number = 1
while current_number <= 5:
    print("current_number = " + str(current_number)) 
    current_number += current_number     
#-------------------------------------------------------------------------------------
active = True
while active:
    message = input(prompt)
    message = message.strip()
    if message == 'q':
       break # force quiting loop
    elif message == 'qq': 
       continue  #  force continuan loop 
    elif message == '':
       active = False
       
    else:
       print(message)

