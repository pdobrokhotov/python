===================== Web API =======================================
A web API is a part of a website designed to interact with programs 
that use very specific URLs to request certain information. 
This kind of request is called an API call. The requested data will
be returned in an easily processed format, such as JSON or CSV. 
Most apps that rely on external data sources, such as apps that 
integrate with social media sites, rely on API calls.
=====================  Git and GitHub ===============================
We’ll base our visualization on information from GitHub, a site that
allows programmers to collaborate on projects. We’ll use GitHub’s API to
request information about Python projects on the site and then generate
an interactive visualization of the relative popularity of these projects 
in Pygal.
==================== Requesting Data Using an API Call ==============
GitHub’s API lets you request a wide range of information through API
calls. To see what an API call looks like, enter the following into your
browser’s address bar and press enter:
https://api.github.com/search/repositories?q=language:python&sort=stars
========================== NOTES ====================================
This call returns the number of Python projects currently hosted on
GitHub, as well as information about the most popular Python repositories.
Let’s examine the call. The first part, https://api.github.com/, directs 
the request to the part of GitHub’s website that responds to API calls. 
The next part, search/repositories, tells the API to conduct a search 
through all repositories on GitHub. The question mark after repositories 
signals that we’re about to pass an argument. The q stands for query, 
and the equal sign lets us begin specifying a query (q=). 
By using language:python, we indicate that we want information only on 
repositories that have Python as the primary language. The final part, 
&sort=stars, sorts the projects by the number of stars they’ve been given.
==================== Installing Requests ===============================
To use the API-functionality install [user requests] package
It allows a Python program to easily request information
from a website and examine the response that’s returned. 
To install it run: "pip install --user requests"
NOTES: When installing you can see the msg below
  WARNING: The script normalizer.exe is installed in 'C:\Users\1\AppData\Roaming\Python\Python310\Scripts' 
   which is not on PATH. Consider adding this directory to PATH or,
   if you prefer to suppress this warning, use --no-warn-script-location.
In this case see
https://www.architectryan.com/2018/03/17/add-to-the-path-on-windows-10/
------------------------------------
Monitoring API Rate Limits
Most APIs are rate-limited, which means there’s a limit to how many requests you can make in a certain amount of time. To see if you’re 
approaching GitHub’s limits, enter
https://api.github.com/rate_limit 
into a web browser. You should see a response like this:
{
"resources": {
"core": {
"limit": 60,
"remaining": 58,
"reset": 1426082320
},........