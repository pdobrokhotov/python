#==============================================================
#================== DEFAULT URLs ==============================
#==============================================================
"""           learning_log URL Configuration
The 'urlpatterns' list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# Since 'url'-lib is depricated since ver=4.0, replace it with 're_path'
"""
#==============================================================
from django.urls import include #,url  
# Since 'url'-lib is depricated since ver=4.0, replace it with 're_path'
from django.urls import re_path    
from django.contrib import admin
#==============================================================
# Below (as in the book) in every INCLUDE() where we also must pass
# a namespace parameter, like include('users.urls', namespace='users')
# but in this version of Django this gives error = app_name is absent 
# Tocorrect error we additionaly pass [app_name] as shown below:
'''
    re_path(r''       , include( ('learning_logs.urls','learning_logs'),
                                namespace= 'learning_logs'
                                )),  
    
''' 
urlpatterns = [
    re_path(r'^admin/', admin.site.urls ),
    # This line will match any URL that starts with the word users, such as  
    # http://localhost:8000/users/login/
    # We also create the namespace 'users' so we’ll be able to distinguish URLs
    # that belong to the learning_logs app from URLs that belong to the users app.
    re_path(r'^users/', include(('users.urls','users'), namespace='users')),
    re_path(r'', include(('learning_logs.urls','learning_logs'),
                         namespace= 'learning_logs')),    

]
#======================================================================         
'''
#==================================================================
# Note, django.conf.urls.url() was deprecated in Django 3.0, 
# and is removed in Django 4.0+. Because we now have version 4.1.2 
# the line below were commented. To cjeck version try
>(ll_env)Django$ django-admin --version
#==================================================================
'''