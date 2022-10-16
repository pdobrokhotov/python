#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# Note, that each time we add a new model, 
# 1) reregister it admin.py. Example: admin.site.register(Topic)
# 2) run the commads below: 
#> CD "D:\My Documents\python\Projects\Django" 
#> ll_env\Scripts\activate
#----------------------------------------------------------
#> (ll_env)Django$ python manage.py makemigrations learning_logs
#> (ll_env)Django$ python manage.py migrate
#> (ll_env)Django$ python manage.py runserver
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
from django.db import models
'''
                 Connecting Data to Certain Users
Now we need to connect the data submitted to the user who submitted it.
We need to connect only the data highest in the hierarchy to a user, and the
lower-level data will follow. For example, in Learning Log, topics are the
highest level of data in the app, and all entries are connected to a topic.
As long as each topic belongs to a specific user, we'll be able to trace the
ownership of each entry in the database.
We'll modify the Topic model by adding a foreign key relationship to a
user. We'll then have to migrate the database. Finally, we'll have to modify
some of the views so they only show the data associated with the currently
logged-in user. For this we use lib = [django.contrib.auth.models import User]
This works because our DB-relationship is = USER->TOPIC->ENTRY
'''
# Import the User model from django.contrib.auth. We then add an owner field
# to Topic, which establishes a foreign key relationship to the User model.
from django.contrib.auth.models import User
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


#======================================================
# Create your models here.
#======================================================
'''
Create a class called Topic, which inherits from Model—a parent
class included in Django that defines the basic functionality of a model.
Only two attributes are in the Topic class: text and date_added.
The text attribute is a CharField—a piece of data that's made up of
characters, or text. We use CharField when we want to store a small
amount of text, such as a name, a title, or a city. 
When we define a CharField attribute, we have to tell Django how much 
space it should reserve in the database. Here we give it a max_length
of 200 characters, which should be enough to hold most topic names.
The date_added attribute is a DateTimeField—a piece of data that will
record a date and time. We pass the argument auto_add_now=True, which
tells Django to automatically set this attribute to the current date 
and time whenever the user creates a new topic. To see the different 
kinds of fields you can use in a model, see: 
https://docs.djangoproject.com/en/1.8/ref/models/fields/
'''

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#A topic the user is learning about 
class Topic(models.Model):
    text       = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    #Add a foreign key relationship to a user. This will allow
    # each user see his own Topic only (and of cousrse this topic entries)
    # We can use either models.CASCADE or models.PROTECT
    owner = models.ForeignKey(User, on_delete=models.PROTECT)
    #====================================================
    # Return a string representation of the model
    def __str__(self):
        return self.text
    '''
    We need to tell Django which attribute to use by default when 
    it displays information about a topic. Django calls  __str__()
    method to display a simple representation of a model. Here we've
    written __str__() method that returns the string stored in 
    the text attribute   
    '''
    #=====================================================
   
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# Something specific learned about a topic 
# We can use either models.CASCADE or models.PROTECT
class Entry(models.Model):
    text       = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    topic      = models.ForeignKey(Topic, on_delete=models.PROTECT)    
    ''' 
    "ForeignKey" is a database term; it's a reference to another record
    in the database. This is the code that connects each entry to a specific
    topic. Each topic is assigned a key, or ID, when it's created. When Django 
    needs to establish a connection between two pieces of data, it uses the 
    key associated with each piece of information. We'll use these connections
    shortly to retrieve all the entries associated with a certain topic.   
    '''
    #====================================================================
    # Nest the Meta class inside our Entry class. Meta holds extra information
    # for managing a model; here it allows us to set a special attribute
    # telling Django to use Entries when it needs to refer to more than one entry.
    class Meta:
        verbose_name_plural = 'entries'
    #====================================================================
    # Return a string representation of the model. It tells Django which
    # information to show when it refers to individual entries. Because 
    # an entry can be a long body of text, we tell Django to show just 
    # the first 50 characters of text. We also add an ellipsis to clarify
    # that we're not always displaying the entire entry.
    def __str__(self):
        return self.text[:50] + "..."
    #====================================================================    
'''
The Entry class inherits from Django's base Model class, just as Topic
did. The first attribute, topic, is a ForeignKey instance v. A foreign key is a
database term; it's a reference to another record in the database. This is the
code that connects each entry to a specific topic. Each topic is assigned a
key, or ID, when it's created. When Django needs to establish a connection
between two pieces of data, it uses the key associated with each piece of
information. We'll use these connections shortly to retrieve all the entries
associated with a certain topic. Next is an attribute called text, which is 
an instance of TextField. This kind of field doesn't need a size limit, 
because we don't want to limit the size of individual entries. 
The date_added attribute allows us to present entries in the order 
they were created and to place a timestamp next to each entry.
(Without this, Django would refer to multiple entries as Entrys.)
'''    
