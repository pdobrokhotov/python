'''
The file views.py in learning_logs was generated automatically 
when we ran the command:  python manage.py startapp
We import the class HttpResponseRedirect, which we'll use to redirect the
reader back to the topics page after they submit their topic. The reverse()
function determines the URL from a named URL pattern, meaning that
Django will generate the URL when the page is requested.
===============================================================================
               Restricting Access with @login_required
===============================================================================               
Django makes it easy to restrict access to certain pages to logged-in users
through the @login_required decorator. A decorator is a directive placed just
before a function definition that Python applies to the function before it
runs to alter how the function code behaves. For this purpose below we import
according module like: from django.contrib.auth.decorators import login_required
To make it work we also # add line = [LOGIN_URL = '/users/login/'] to settings.py
----------------------------------------------------------------------------
Django makes it easy to restrict access to pages, but you have to decide
which pages to protect. It's better to think about which pages need to be
unrestricted first and then restrict all the other pages in the project. 
You can easily correct overrestricting access, and it's less dangerous than 
leaving sensitive pages unrestricted. In Learning Log, we'll keep the home page, 
the registration page, and logout unrestricted. We'll restrict access to every
other page. Thus, here we apply this decorators to every view except index():
'''
# Module renders the response based on the data provided by views
from django.shortcuts import render
# Make sure user sees only his own topics even when he tried to trick access
# using for exanple URL = http://localhost:8000/topics/1/ thst is not his'
from django.http import HttpResponseRedirect, Http404

# Modules needed for new_topic() function (request,process and redirect)
from django.http import HttpResponseRedirect
# The module below was depricated and we use [django.urls] instead
# from django.core.urlresolvers import reverse  (from book)
from django.urls import reverse  # modified by me)
#-----------------------------------------------------------------------
# Each topic will be owned by a user, so only registered users should 
# be able to request the topics page.(see page 447)
from django.contrib.auth.decorators import login_required
#-----------------------------------------------------------------------
# Model associated with Topics\Entry pages
from .models import Topic, Entry
# Model associated with User Forms (Example: def new_topic(request))
from .forms import TopicForm, EntryForm

#===============================================================
# Create your views here.
#===============================================================
# The home page for Learning Log 
def index(request):
    return render(request, 'learning_logs/index.html')
#================================================================ 
# Show all topics.
'''
Django makes it easy to restrict access to certain pages to logged-in users
through the [login_required] decorator. A decorator is a directive placed just
before a function definition that Python applies to the function before it
runs to alter how the function code behaves. For this purpose below we import
according module like: from django.contrib.auth.decorators import login_required
We first import the login_required() function. We it as a decorator to the 
topics() view function by prepending login_required with the @ symbol so Python
knows to run the code in login_required() before the code in topics().
The code in login_required() checks to see if a user is logged in, and
Django will run the code in topics() only if they are. If the user is not
logged in, they're redirected to the login page. To make it work we also
add line = [LOGIN_URL = '/users/login/'] to  settings.py
'''
# Decorator we can use after import [django.contrib.auth.decorators]
@login_required 
def topics(request):
    # query the database by asking for the Topic objects, sorted  
    # by the date_added attribute and store the result in topics.
    '''
    When a user is logged in, the request object has a request.user attribute
    set that stores information about the user. The function filter() tells 
    Django to retrieve only the Topic objects from the database whose owner 
    attribute matches the current user. Because we're not changing how the 
    topics are displayed, we don't need to change the template for the topics
    page at all.
    '''
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    # define a context that we???ll send to the template. A context 
    # is a dictionary in which the keys are names we???ll use in the 
    # template to access the data and the values are the data we 
    # need to send to the template. In this case, there???s one 
    # key-value pair, which contains the set of topics we will 
    # display on the page.
    context = {'topics': topics}
    # When building a page that uses data, we pass the context variable
    # to render() as well as the request object and the path to the template
    return render(request, 'learning_logs/topics.html', context)
#================================================================ 
# Show a single topic and all its entries. 
# Decorator we can use after import [django.contrib.auth.decorators]
@login_required 
def topic(request, topic_id):
    ''' 
    This is the first view function that requires a parameter other 
    than the request object. The function accepts the value captured by
    the expression (?P<topic_id>\d+) and stores it in topic_id 
    The code phrases [topic] and [entries] variables are called queries, 
    because they query the database for specific information
    '''
    # get\query the given topic from all objects by its ID
    topic = Topic.objects.get(id=topic_id)
    # Make sure the topic belongs to the current user. Because he may
    # trick his access using URL for a topic, created by another user
    if topic.owner != request.user:
       raise Http404
    # get\query the entries associated with this topic, and we order 
    # them according to date_added: the minus sign in front of 
    # date_added sorts the results in reverse order, which will 
    # display the most recent entries first.  
    entries = topic.entry_set.order_by('-date_added')
    # store the topic entries in the context dictionary
    context = {'topic': topic, 'entries': entries}
    # send context to the template topic.html
    return render(request, 'learning_logs/topic.html', context) 
#================================================================
#  Render a form for a new topic. 
'''
You use GET requests for pages that only read data from the server. 
You usually use POST requests when the user needs to submit information
through a form. We'll be specifying the POST method for processing all 
of our forms. Thus function takes in the request object as a parameter.
When the user initially requests this page, their browser will send a GET
request. When the user has filled out and submitted the form, their browser
will submit a POST request. Depending on the request, we'll know if
the user is requesting a blank form (a GET request) or asking us to process
a completed form (a POST request).
'''
# Decorator we can use after import [django.contrib.auth.decorators]
@login_required 
def new_topic(request):
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = TopicForm()
    else:
        # POST data submitted; process data.
        # Thus, make an instance of TopicForm and pass it
        # the data entered by the user, stored in request.POST. 
        # The form object that???s returned contains the information 
        # submitted by the user
        form = TopicForm(request.POST)
        if form.is_valid(): # if data valid (for example fileds are non empty)
            '''
            We MUST associate new topics with any particular user. 
            Because if NOT, the when we try adding a new topic,we'll 
            see the error message IntegrityError along with message:
            [learning_logs_topic.user_id may not be NULL]. 
            Django's saying you can't create a new topic without
            specifying a value for the topic's owner field. 
            There's a straightforward fix for this problem, because 
            we have access to the current user through the request object
            When we first call form.save(), we pass the commit=False argument
            because we need to modify the new topic before saving it to the 
            database. We then set the new topic's owner attribute to the current
            user. Finally, we call save() on the topic instance just defined. 
            Now the topic has all the required data and will save successfully.
            '''
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save() # write the data from the form to the database
            # Once we???ve saved the data, we can leave this page. 
            # We use reverse() to get the URL for the topics page and pass
            # the URL to HttpResponseRedirect(), which redirects the user's 
            # browser to the topics page. On the topics page, the user should
            # see the topic they just entered in the list of topics.
            return HttpResponseRedirect(reverse('learning_logs:topics'))
    # Send the form to the template in the context dictionary variable   
    context = {'form': form} # dictionary with one item (form object variable)
    return render(request, 'learning_logs/new_topic.html', context)
 
#================================================================ 
# Add a new entry for a particular topic.
# The definition of new_entry() has a topic_id parameter to store the value it
# receives from the URL. We???ll need the topic to render the page and process
# the form???s data, so we use topic_id to get the correct topic object 
# Decorator we can use after import [django.contrib.auth.decorators]
@login_required 
def new_entry(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = EntryForm()
    else:
        # POST data submitted; process data.
        form = EntryForm(data=request.POST)
        if form.is_valid():
            # When we call save(), we include the argument commit=False
            # to tell Django to create a new entry object and store it in
            # new_entry without saving it to the database yet.
            new_entry = form.save(commit=False)
            # set new_entry???s topic attribute to the topic we pulled
            # from the database at the beginning of the function and 
            # then we call save() with no arguments. This saves the 
            # entry to the database with the correct associated topic.
            new_entry.topic = topic
            new_entry.save()
            # Redirect the user to the topic page. The reverse() call 
            # requires two arguments: the name of the URL pattern we want
            # to generate a URL for and an args list containing any arguments
            # that need to be included in the URL. The args list has one item
            # in it = topic_id. The HttpResponseRedirect() call then redirects 
            # the user to the topic page they made an entry for, and they 
            # should see their new entry in the list of entries.
            return HttpResponseRedirect(reverse('learning_logs:topic', 
                                                args=[topic_id]))
    # Send the form to the template in the context dictionary variable         
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)
#================================================================
# Edit an existing entry. 
# Decorator we can use after import [django.contrib.auth.decorators]
@login_required 
def edit_entry(request, entry_id):
    # get the entry object that the user wants to edit and the topic 
    # associated with this entry
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    # Make sure the entry belongs to the current user. Because he may
    # trick his access using URL for an entry, created by another user
    if topic.owner != request.user:  
        raise Http404   
    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry.
        # Make an instance of EntryForm with the argument instance=entry
        # This argument tells Django to create the form prefilled with 
        # information from the existing entry object. The user will see 
        # their existing data and be able to edit that data.
        form = EntryForm(instance=entry)
    else: 
        # POST data submitted; process data.
        # When processing a POST request, we pass the instance=entry argument
        # and the data=request.POST argument w to tell Django to create a form
        # instance based on the information associated with the existing entry
        # object, updated with any relevant data from [request.POST]
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            # redirect to the topic page y, where the user should see the 
            # updated version of the entry they edited.
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic.id]))
    # Send the form to the template in the context dictionary variable              
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)
#================================================================ 
