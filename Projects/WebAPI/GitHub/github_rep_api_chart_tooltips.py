import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS
#========================================================================
my_style = LS('#333366', base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
chart.title = 'Python Projects with Bar Tooltips'
chart.x_labels = ['httpie', 'django', 'flask']
#========================================================================
plot_dicts = [{'value': 16101, 'label': 'Description of httpie.'},
              {'value': 15028, 'label': 'Description of django.'},
              {'value': 14798, 'label': 'Description of flask.'},
              ]
chart.add('', plot_dicts)
# Save chart to file
chart.render_to_file('Projects\WebAPI\GitHub\GitHubBarChartTooltips.svg')
#=================================================================
'''
First wedefine a list called plot_dicts that contains three dictionaries:
one for the HTTPie project, one for the Django project, and one for Flask.
Each dictionary has two keys: 'value' and 'label'. Pygal uses the number
associated with 'value' to figure out how tall each bar should be, and it
uses the string associated with 'label' to create the tooltip for each bar. 
For example, the first dictionary will create a bar representing a project
with 16101 stars, and its tooltip will say "Description of httpie".
The add() method needs a string and a list. When we call add(), we pass
in the list of dictionaries representing the bars (plot_dicts). 
Pygal includes the number of stars as a default tooltip in addition 
to the custom tooltip we passed it.

'''