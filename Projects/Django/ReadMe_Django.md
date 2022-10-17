================  Getting Started with Django ===================
Django is a high-level Python web framework that encourages rapid 
development and clean, pragmatic design. Built by experienced 
developers, it takes care of much of the hassle of web development, 
so you can focus on writing your app without needing to reinvent 
the wheel. It’s free and open source.
Behind the scenes, today’s websites are
actually rich applications that act like fully
developed desktop applications. Python has
a great set of tools for building web applications.
In this chapter you’ll learn how to use Django
(http://djangoproject.com/) to build a web-project 
called "Learning Log—an online journal system" that
lets you keep track of information you’ve learned about
particular topics.

===================================================================
============== Creating a Virtual Environment =====================
===================================================================

To work with Django, we’ll first set up a virtual environment to work in. A
virtual environment is a place on your system where you can install packages
and isolate them from all other Python packages. Separating one project’s
libraries from other projects is beneficial and will be necessary when we
deploy Learning Log to a server. 
Create a new directory for your project called Django, switch to
that directory in a terminal, and create a virtual environment. 
If you're using Python 3, you should be able to create a virtual 
environment with the following command:
> CD D:
> CD D:\My Documents\python\Projects\Django
> python -m venv ll_env
Here we're running the "venv"-module and using it to create 
a virtual environment named = "ll_env"
------------------------- NOTE ----------------------------------
If it doesn’t work, you need to install "virtualenv"
> pip install --user virtualenv
Then change to the Django directory in a terminal, and create 
a virtual environment like this:
> CD D:
> CD D:\My Documents\python\Projects\Django
> virtualenv ll_env
-------------------------------------------------------------------

=====================================================================
========================= Activate environment ======================
=====================================================================
The command below runs the script activate in ll_env/bin.
Для Windows
> CD "D:\My Documents\python\Projects\Django" 
> ll_env\Scripts\activate
Для Линукс
> source ll_env/bin/activate

When the environment is active, you’ll see the name of the 
environment in parentheses in the command prompt
> (ll_env)Django$ 
Then you can install packages to the environment and use packages 
that have already been installed. Packages you install in "ll_env"
will be available only while the environment is active
To stop using a virtual environment, enter deactivate:
> (ll_env)Django$ deactivate
The environment will also become inactive if you close 
the terminal it’s running in.
==========================================================
================== Installing Django =====================
==========================================================
NOTE: The code in book is based on older version = 3.2
Thus, better install lt instead id the latest one
> (ll_env)Django$ pip install django==3.2.10
---------------------------------------------------------
To install the latest version ( 4.1.2) run:
> (ll_env)Django$ pip install Django
 or better
> (ll_env)Django$ py -m pip install Django
---------------------------------------------------------
Keep in mind that Django will be available only when the 
environment is active. (it seems to be installed on C:)
Verify version (we have = 4.1.2)
>(ll_env)Django$ django-admin --version

==========================================================
============ Creating a Project in Django ================
==========================================================
Without leaving the active virtual environment (remember to look for 
ll_env in parentheses), enter the following commands to create a new project:
> (ll_env)Django$ django-admin startproject learning_log .
Note, that the point (".") in the end of command above is NEEDED!
=============================================================

In folder = Django is created a new folder called learning_log. 
It also created a file called "manage.py", which is a short program
that takes in commands and feeds them to the relevant part of Django 
to run them. We’ll use these commands to manage tasks like working 
with databases and running servers.
The learning_log directory contains four files w, the most important
of which are :
- settings.py  
- urls.py  
- wsgi.py
- manage.py
The settings.py file controls how Django interacts with your system 
and manages your project. We’ll modify a few of these settings and 
add some settings of our own as the project evolves. 
The urls.py file tells Django which pages to build in response to
browser requests. The wsgi.py file helps Django serve the files it 
creates. The filename is an acronym for web server gateway interface.
===================================================================
================ Creating the Database (SQL-Lite)==================
===================================================================
SQL-Lite DB is a single file (db.sqlite3) and it’s ideal for writing
simple apps because you won’t have to pay much attention to managing
the database. Any time we modify a database, we say we’re migrating 
the database.
> python manage.py migrate
Issuing the migrate command for the first time tells Django to make sure the
database matches the current state of the project. The first time we run this
command in a new project using SQLite (more about SQLite in a moment),
Django will create a new database for us. At u Django reports that it will
make the database tables needed to store the information we’ll use in this
project (Synchronize unmigrated apps), and then make sure the database
structure matches the current code (Apply all migrations).
======================================================================
================= Viewing the Project ================================
======================================================================
Let’s make sure that Django has set up the project properly. 
Enter the runserver command as follows:
> (ll_env)Django$ python manage.py runserver
Django starts a server so you can view the project on your system to see
how well it works. When you request a page by entering a URL in a browser,
the Django server responds to that request by building the appropriate
page and sending that page to the browser.
Then on the screen you'll see IP-address you can use
whule the Gjango server is still running
.....................................
System check identified no issues (0 silenced).
October 13, 2022 - 16:52:56
Django version 4.1.2, using settings 'learning_log.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
......................................
NOTE: If you receive the error message That port is already in use, 
tell Django to use a different port by entering 
> python manage.py runserver 8001 
and cycle through higher numbers until you find an open port.
=============================================================
==================== Starting an App ========================
=============================================================
> CD "D:\My Documents\python\Projects\Django" 
> ll_env\Scripts\activate
> python manage.py startapp learning_logs
The command startapp appname tells Django to create the infrastructure
needed to build an app. If you look in the project directory now, you’ll see
a new folder called learning_logs. Open that folder to see what Django has
created. The most important files are models.py, admin.py, and views.py.
We’ll use models.py to define the data we want to manage in our app. We’ll
get to admin.py and views.py a little later.
==============================================================
===================== Activating Models ======================
==============================================================
To use our models, we have to tell Django to include our app in the overall
project. Open settings.py (in the learning_log/learning_log directory), and
you’ll see a section that tells Django which apps are installed in the project:
Add our app name as shown below
-----------------------------
INSTALLED_APPS = (
--snip--
'django.contrib.staticfiles',
# My apps
'learning_logs',
)
-----------------------------
==============================================================
================= MODIFY DB ==================================
==============================================================
Next, we need to tell Django to modify the database so it can 
store information related to the model Topic. From the terminal, 
run the following command:
> python manage.py makemigrations learning_logs
The command makemigrations tells Django to figure out how to modify
the database so it can store the data associated with any new models
we’ve defined. The output here shows that Django has created a migration
file called 0001_initial.py. This migration will create a table for the
model = Topic in the database
After we apply this migration and have Django modify the database
for us run:
> python manage.py migrate
Whenever we want to modify the data that Learning Log manages,
we’ll follow these three steps: 
- modify models.py
- call makemigrations on learning_logs
- tell Django to migrate the project.
========================================================================
==================== Create DB-admin ===================================
========================================================================
To create a superuser in Django, enter the following command and
respond to the prompts:
> python manage.py createsuperuser
-----------------------------------------------
Username (leave blank to use '1'): sa
Email address:  ******
Password: ****** 
Password (again): ****** 
Superuser created successfully.
-----------------------------------------------

===============================================
=== Registering a Model with the Admin Site ===
===============================================
Django includes some models in the admin site automatically, 
such as User and Group, but the models we create need to be 
registered manually. To do this edit a file called admin.py 
in the same directory as models.py and enter
------------------------------
from django.contrib import admin
from learning_logs.models import Topic
admin.site.register(Topic)
------------------------------
This code imports the model we want to register = Topic, and then uses
admin.site.register() to tell Django to manage our model through the
admin site. Now use the superuser account to access the admin site. 
Go to http://localhost:8000/admin/
or
      http://127.0.0.1:8000/admin/    
enter the username and password for the superuser
you just created, and you should see a page allows you to add new users 
and groups and change existing ones. We can also work with data related 
to the Topic model that we just defined.
--------------------------------------------------------
NOTE: If you see a message in your browser that the web page is not available, make sure you still have the Django server running in a terminal window. If you don’t, activate a virtual environment and reissue the command :
> python manage.py runserver
============================================================
=============== The Django Shell ===========================
============================================================
Now that we’ve entered some data, we can examine that data programmatically
through an interactive terminal session. This interactive environment is
called the Django shell, and it’s a great environment for testing and
troubleshooting your project. Here’s an example of an interactive shell 
session:
-----------------------------------------------------------
> CD "D:\My Documents\python\Projects\Django"
> ll_env\Scripts\activate
> (ll_env)Django$ python manage.py shell
  >>> from learning_logs.models import Topic
  >>> Topic.objects.all()
Result on screen : <QuerySet [<Topic: topic 1>, <Topic: topic 2>]>
============================================================
==================== The django-bootstrap3 App =============
============================================================
We’ll use django-bootstrap3 to integrate Bootstrap into our project. This
app downloads the required Bootstrap files, places them in an appropriate
location in your project, and makes the styling directives available in your
project’s templates.To install django-bootstrap3, issue the following command
in an active virtual environment:
> (ll_env)learning_log$ pip install django-bootstrap3
============================================================
================= Try It Yourself ==========================
============================================================
20-1. Other Forms: We’ve applied Bootstrap’s styles for the
login and add_topic pages. Make similar changes to the rest 
of the form-based pages: 
- new_entry
- edit_entry
- register
============================================================
================= Deploy site to Internet Host =============
============ Installing the Heroku Toolbelt ================
============================================================
We'll use free hosting on https://www.heroku.com/
Register there first
To deploy and manage a project on Heroku’s servers, you’ll need the tools
available in the Heroku Toolbelt. To install the latest version of the Heroku
Toolbelt, visit https://toolbelt.heroku.com/ and follow the directions for your operating system, which will include either a one-line terminal command
or an installer you can download and run.
-------------- Installing Required Packages -------------------
You’ll also need to install a number of packages that help serve Django projects on a live server. In an active virtual environment, issue the following commands:
(ll_env)Django$ pip install dj-database-url
(ll_env)Django$ pip install dj-static
(ll_env)Django$ pip install static3
(ll_env)Django$ pip install gunicorn
















