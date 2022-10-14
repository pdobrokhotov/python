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
"""
from django.urls import include, re_path
#==============================================================

urlpatterns = [
    re_path( r'^admin/', include('learning_logs.urls') ),
    re_path(r'', include('learning_logs.urls')),
    ]
#======================================================================         
'''
#==================================================================
# Note, django.conf.urls.url() was deprecated in Django 3.0, 
# and is removed in Django 4.0+. Because we now have version 4.1.2 
# the line below were commented. To cjeck version try
>(ll_env)Django$ django-admin --version
#==================================================================
from django.conf.urls import include, url 
from django.contrib import admin
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('learning_logs.urls', namespace='learning_logs')),# from book
    ]
#===============================================================================


'''