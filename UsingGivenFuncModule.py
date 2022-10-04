# ============== import 2 specific functions ONLY with their names ===============
from my_funct_module import build_profile, make_pizza 
# We could also use this syntacse to import all fuinction: from pizza import *
#=============== import 2 specific functions ONLY with their aliases =============
#       from my_funct_module import build_profile as bp, make_pizza as mp 
#       mp('16', 'pepperoni') 
#================= NOTE ==========================================================
#we could use "import my_funct_module" to import ALL functions from my_funct_module.py
# But in the latter case we MUST cal them like below, indicating Module Name:
# my_funct_module.make_pizza('12', 'mushrooms', 'green peppers', 'extra cheese')
#=================================================================================
print("====== Call function = build_profile from attached module ============")   
user_profile =  build_profile('albert', 'einstein',location='princeton',field='physics')
print(user_profile)
#=================================================================================
print("====== Call function = make_pizza from attached module ============")   
make_pizza('12', 'mushrooms', 'green peppers', 'extra cheese')