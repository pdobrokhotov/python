'''
The file views.py in learning_logs was generated automatically 
when we ran the command:  python manage.py startapp
'''
# Module renders the response based on the data provided by views
from django.shortcuts import render
# Model associated with Topics-page
from .models import Topic

#===============================================================
# Create your views here.
#===============================================================
# The home page for Learning Log 
def index(request):
    #pass
    #return render(request, 'Django/templates/learning_logs/index.html')
    return render(request, 'learning_logs/index.html')
#===========================================================================
# Show all topics. 
def topics(request):
    # query the database by asking for the Topic objects, sorted  
    # by the date_added attribute and store the result in topics.
    topics = Topic.objects.order_by('date_added')
    # define a context that we’ll send to the template. A context 
    # is a dictionary in which the keys are names we’ll use in the 
    # template to access the data and the values are the data we 
    # need to send to the template. In this case, there’s one 
    # key-value pair, which contains the set of topics we will 
    # display on the page.
    context = {'topics': topics}
    # When building a page that uses data, we pass the context variable
    # to render() as well as the request object and the path to the template
    return render(request, 'learning_logs/topics.html', context)

