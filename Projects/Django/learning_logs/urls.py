#========================================================
#=============== APP URLS ===============================
#========================================================
"""
Defines URL patterns for learning_logs.
The default urls.py is in the learning_log folder; 
But here on [learning_logs folder] we make a second urls.py 
file for our APP
"""
# We then import the url function, which is needed when mapping URLs to views
from django.urls import re_path
# the dot tells Python import views from the same directory as the 
# current urls.py module. The variable urlpatterns in this module
# is a list of individual pages that can be requested from the 
# learning_logs app
from . import views

#==============================================================
# The actual URL pattern is a call to the url() function, which
# takes three arguments y. The first is a regular expression. 
# Django will look for a regular expression in urlpatterns that 
# matches the requested URL string. Therefore, a regular expression
# will define the pattern that Django can look for.
# When a URL request matches the pattern we just defined, Django 
# will look for a function called index() in the views.py file

urlpatterns = [
    # Home page
    re_path(r'^$', views.index, name='index'),
    # Show all topics. Any request with a URL that matches this pattern
    # will then be passed to the function topics() in views.py.
    re_path(r'^topics/$', views.topics, name='topics'),
    # Detail page for a single topic
    # It forms URL like: http://localhost:8000/topics/1/
    re_path(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
    # Page for adding a new topic
    # It forms URL like: http://localhost:8000/new_topic/.
    re_path(r'^new_topic/$', views.new_topic, name='new_topic'),
    # Pags to add\edit a new entry
    # It forms URL like: http://localhost:8000/new_entry/id/, 
    # where id is a number matching the topic ID
    re_path(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
    re_path(r'^edit_entry/(?P<entry_id>\d+)/$',views.edit_entry,name='edit_entry'),
    
    ]
'''
#==================================================================
# Note, django.conf.urls.url() was deprecated in Django 3.0, 
# and is removed in Django 4.0+. Because we now have version 4.1.2 
# the line below were commented. To check version try
>(ll_env)Django$ django-admin --version
#==================================================================
from django.conf.urls import url
from . import views
urlpatterns = [
    # Home page
    url(r'^$', views.index, name='index'),
    ]
#==================================================================





-------------------- url(r'^$', views.index, name='index')-----------------
the regular expression r'^$'. The r tells Python to interpret
the following string as a raw string, and the quotes tell Python where
the regular expression begins and ends. The caret (^) tells Python to
find the beginning of the string, and the dollar sign tells to look
for the end of the string. In its entirety, this expression tells Python to
look for a URL with nothing between the beginning and end of the URL.
Python ignores the base URL for the project (http://localhost:8000/), 
so an empty regular expression matches the base URL.
Any other URL will not match this expression, and Django will return 
an error page if the URL requested doesn't match any existing URL patterns.
The second argument in url() at y specifies which view function
to call. When a requested URL matches the regular expression, Django
will call views.index (we'll write this view function in the next section).
The third argument provides the name index for this URL pattern so we
can refer to it in other sections of the code. Whenever we want to provide
a link to the home page, we'll use this name instead of writing out a URL.
==========================================================================
Let's examine the regular expression in this URL pattern, r'^topics/
(?P<topic_id>\d+)/$'. The r tells Django to interpret the string as a raw
string, and the expression is contained in quotes. The second part of the
expression, /(?P<topic_id>\d+)/, matches an integer between two forward
slashes and stores the integer value in an argument called topic_id. The
parentheses surrounding this part of the expression captures the value
stored in the URL; the ?P<topic_id> part stores the matched value in
topic_id; and the expression \d+ matches any number of digits that appear
between the forward slashes.
When Django finds a URL that matches this pattern, it calls the view
function topic() with the value stored in topic_id as an argument. We'll use
the value of topic_id to get the correct topic inside the function.

The code (?P<topic_id>\d+) captures a numerical value and stores it in the variable
topic_id. When a URL matching this pattern is requested, Django sends the
request and the ID of the topic to the new_entry() view function.
'''