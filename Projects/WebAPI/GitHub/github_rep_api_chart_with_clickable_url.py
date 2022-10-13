'''        Plotting the Data (Clickable chart)
Now that we have some interesting data, let's make a visualization showing
the relative popularity of Python projects on GitHub. We'll make an interactive
bar chart: the height of each bar will represent the number of stars the project
has acquired. To plot our data, we'll generate plot_dicts automatically 
for the 30 projects returned by the API call.
Clicking a bar will take you to that project's home on GitHub.
'''

# Import API-requests lib
import requests
# Import pygal and the Pygal styles libs
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS
#===========================================================
# Make an API call and store the response.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code:", r.status_code) # Status=200 indicates a success.
# Store API response ( in JSON format) in a variable.
response_dict = r.json()
print("Total repositories:", response_dict['total_count'])
#===========================================================
# Explore information about the repositories.
repo_dicts = response_dict['items'] # Store this list of dictionaries
'''
We'll need the name of each project in order to label the bars, 
and the number of stars to determine their height. In the loop, 
we append the name of each project and number of stars it has 
to these lists. But now we'll modify the commands below to use
list od dictionaries instead od simple list:
 
names, stars = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])
'''
names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    # Pygal uses the URL associated with 'xlink' to turn 
    # each bar into an active link
    plot_dict = {'value': repo_dict['stargazers_count'],
                 'label': repo_dict['description'],
                 'xlink': repo_dict['html_url'],
                 }
    plot_dicts.append(plot_dict)
    
#===========================================================    
# Make visualization using style-lubrary and configure it
#===========================================================   
# Define a style using the LightenStyle class (alias LS) 
# and base it on a dark shade of blue. We also pass the 
# base_style argument to use the LightColorizedStyle class (alias LCS).
my_style = LS('#333366', base_style=LCS)
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000
# Make a simple bar chart and pass it all configurations above
chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = names
# Method "chart.y_labels = stars" gives error. Use use add-method instead
chart.add('', plot_dicts)
# Save chart to file
chart.render_to_file('Projects\WebAPI\GitHub\GitHubReposClickableURL.svg')

'''
First we make an instance of Pygal's Config class, called my_config;
modifying the attributes of my_config will customize the appearance of the
chart. We set the two attributes x_label_rotation and show_legend, originally
passed as keyword arguments when we made an instance of Bar. Then we set the 
font size for the chart's title, minor labels, and major labels. 
The minor labels in this chart are the project names along the x-axis and most
of the numbers along the y-axis. The major labels are just the labels on the
y-axis that mark off increments of 5000 stars. These labels will be larger,
which is why we differentiate between the two. At x we use truncate_label to
shorten the longer project names to 15 characters. (When you hover over a
truncated project name on your screen, the full name will pop up.) Next,
we hide the horizontal lines on the graph by setting show_y_guides to False y.
Finally, we set a custom width so the chart will use more of the available
space in the browser.
'''

