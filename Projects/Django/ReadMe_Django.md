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
The environment will also become inactive if you close the terminal 
it’s running in.
==========================================================
================== Installing Django =====================
==========================================================
> (ll_env)Django$ pip install Django
 or better
> (ll_env)Django$ py -m pip install Django

Keep in mind that Django will be available only when the 
environment is active. (it seems to be installed on C:)
Verify version
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


