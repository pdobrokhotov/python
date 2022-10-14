'''
The file views.py in learning_logs was generated automatically 
when we ran the command:  python manage.py startapp
'''
# Module renders the response based on the data provided by views
from django.shortcuts import render
#===============================================================
# Create your views here.
#===============================================================

# The home page for Learning Log 
def index(request):
    #pass
    #return render(request, 'Django/templates/learning_logs/index.html')
    return render(request, 'learning_logs/index.html')


