'''
One excellent resource for exploring the
Python standard library is a site called Python Module of the Week. Go to
http://pymotw.com/ and look at the table of contents. Find a module that
looks interesting to you and read about it, or explore the documentation of
the collections and random modules.
'''

# this class is like Dictionary but keeps the order new key-pairs are added
from collections import OrderedDict # works as ordered Dictionary
# create an instance of the OrderedDict class. Notice there are no curly brackets; the call to OrderedDict() 
# creates an empty ordered dictionary for us and stores it in favorite_languages. We then add each name and language
# to favorite_languages one at a time
favorite_languages = OrderedDict() 
# add new key-pairs to clas as if it were a list. This is a great class to be aware of 
# because it combines the main benefit # of lists (retaining your original order) with 
# the main feature of dictionaries (connecting pieces of information).
favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'
#loop names-lamguages key-value pairs (hust like it were Dictionary)
for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")
#==============================================================================
from random import randint
x = randint(1, 6)
print(x)
#==============================================================================


