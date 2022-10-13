======================== The Django Shell =================================
Now that we’ve entered some data, we can examine that data programmatically
through an interactive terminal session. This interactive environment is
called the Django shell, and it’s a great environment for testing and troubleshooting
your project. Here’s an example of an interactive shell session:
(ll_env)learning_log$ python manage.py shell
u >>> from learning_logs.models import Topic
>>> Topic.objects.all()
[<Topic: Chess>, <Topic: Rock Climbing>]
The command python manage.py shell (run in an active virtual environment)
launches a Python interpreter that you can use to explore the data
stored in your project’s database. Here we import the model Topic from the
learning_logs.models module u. We then use the method Topic.objects.all()
to get all of the instances of the model Topic; the list that’s returned is called
a queryset.
We can loop over a queryset just as we’d loop over a list. Here’s how you
can see the ID that’s been assigned to each topic object:
>>> topics = Topic.objects.all()
>>> for topic in topics:
Getting Started with Django 411
... print(topic.id, topic)
...
1 Chess
2 Rock Climbing
We store the queryset in topics, and then print each topic’s id attribute
and the string representation of each topic. We can see that Chess has an
ID of 1, and Rock Climbing has an ID of 2.
If you know the ID of a particular object, you can get that object and
examine any attribute the object has. Let’s look at the text and date_added
values for Chess:
>>> t = Topic.objects.get(id=1)
>>> t.text
'Chess'
>>> t.date_added
datetime.datetime(2015, 5, 28, 4, 39, 11, 989446, tzinfo=<UTC>)
We can also look at the entries related to a certain topic. Earlier we
defined the topic attribute for the Entry model. This was a ForeignKey, a connection
between each entry and a topic. Django can use this connection to
get every entry related to a certain topic, like this:
u >>> t.entry_set.all()
[<Entry: The opening is the first part of the game, roughly...>, <Entry: In
the opening phase of the game, it's important t...>]
To get data through a foreign key relationship, you use the lowercase
name of the related model followed by an underscore and the word set u.
For example, say you have the models Pizza and Topping, and Topping is
related to Pizza through a foreign key. If your object is called my_pizza,
representing a single pizza, you can get all of the pizza’s toppings using
the code my_pizza.topping_set.all().
We’ll use this kind of syntax when we begin to code the pages users
can request. The shell is very useful for making sure your code retrieves
the data you want it to. If your code works as you expect it to in the shell,
you can expect it to work properly in the files you write within your project.
If your code generates errors or doesn’t retrieve the data you expect it to,
it’s much easier to troubleshoot your code in the simple shell environment
than it is within the files that generate web pages. We won’t refer to the shell
much, but you should continue using it to practice working with Django’s
syntax for accessing the data stored in the project.