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
to these lists
'''
names, stars = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])
    
#===========================================================    
# Make visualization using style-lubrary
#===========================================================   
# Define a style using the LightenStyle class (alias LS) 
# and base it on a dark shade of blue. We also pass the 
# base_style argument to use the LightColorizedStyle class (alias LCS).
my_style = LS('#333366', base_style=LCS)
# Make a simple bar chart and pass it my_style
'''
We pass pass it my_style and two more style arguments: we set the rotation 
of the labels along the x-axis to 45 degrees (x_label_rotation=45),and we 
hide the legend, because we're plotting only one series on the chart
(show_legend=False). We then give the chart a title and set the x_labels 
attribute to the list names.
'''
chart = pygal.Bar(style=my_style, 
                  x_label_rotation=45, 
                  show_legend=False)
chart.title = 'Most-Starred Python Projects on GitHub'
# Set labels for x-axis
chart.x_labels = names
# Method "chart.y_labels = stars" gives error. Use use add-method instead
chart.add('', stars)  
# Save chart to file
chart.render_to_file('Projects\WebAPI\GitHub\GitHubRepos.svg')