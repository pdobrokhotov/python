import my_funct_module as myfunc # import all functions from my_funct_module.py using alias for it
# from my_funct_module import build_profile, make_pizza # import 2 specific functions ONLY
# in this case we can call functions without module name
# We could also use this syntacse to import all fuinction: from pizza import *
#==============================================================
print("====== Call function = build_profile from attached module ============")  
# because we used alias we c al dunction using it = myfunc.build_profile
# But we might not want to use alias then we'd cal function =  my_funct_module.build_profile
user_profile =  myfunc.build_profile('albert', 'einstein',location='princeton',field='physics')
print(user_profile)
#==============================================================
print("====== Call function = make_pizza from attached module ============")   
myfunc.make_pizza('12', 'mushrooms', 'green peppers', 'extra cheese')

#==================================================================================
print("\n====== Call function = count_words from attached module ============\n") 
filenames = ['file_to_write_in.txt', 'not_existing.txt', 'pi_digits.txt', 'README.md']
for filename in filenames:
    myfunc.count_words(filename,True) 
print ("\n")
for filename in filenames:
    myfunc.count_words(filename ) 