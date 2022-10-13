from django.contrib import admin

# Register your models here.
from learning_logs.models import Topic
admin.site.register(Topic)
'''
This code imports the model we want to register = Topic, and then uses
admin.site.register() to tell Django to manage our model through the
admin site. Now use the superuser account to access the admin site. 
Go to http://localhost:8000/admin/, 
enter the username and password for the superuser
you just created, and you should see a page allows you to add new users 
and groups and change existing ones. We can also work with data related 
to the Topic model that we just defined.

'''