# Defines URL patterns for users.The command below from book is depricated 
# from django.conf.urls import url
from django.urls import re_path as url 
#----------------------------------------------------------------------------
# Import the default login view. Nite, that [django.contrib.auth.views]
# is depricated, Thus, instead of it we use [django.contrib.auth]
# from django.contrib.auth.views import login # this is depricated
from django.contrib.auth import views as login
#----------------------------------------------------------------------------
from . import views
''' 
When Django reads this URL, the word users tells Django 
to look in users/urls.py, and login tells it to send requests to 
Django's default login view (notice the view argument is login, 
not views.login). Because we're not writing our own view function, 
we pass a dictionary telling Django where to find the template we're 
about to write. This template will be part of the users app, 
not the learning_logs app. The line below from book is depricated:
# Login page. 
  url(r'^login/$', login, {'template_name': 'users/login.html'},name='login'),
# Logout page
  url(r'^logout/$', views.logout_view, name='logout'),
'''
urlpatterns = [
    # Login page. 
    url(r'^login/$', 
        login.LoginView.as_view(template_name='users/login.html'),
        name='login'), 
    # Logout page
    url(r'^logout/$', views.logout_view, name='logout'),
    # Registration page. Allow new users to register. We’ll use Django’s
    # default UserCreationForm but write our own view function and template
    # This pattern matches the URL http://localhost:8000/users/register/ 
    # and sends requests to the register() function in 'users/views.py'
    url(r'^register/$', views.register, name='register'),
    
]