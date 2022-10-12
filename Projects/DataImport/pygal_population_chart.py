import pygal
#=========================================================
'''
First make an instance of the Worldmap class and set the map's title
attribute. Then use the add() method, which takes in a label and a list of
country codes for the countries we want to focus on. Each call to add() sets
up a new color for the set of countries and adds that color to a key on the
left of the graph with the label specified here. We want the entire region of
North America represented in one color, so we place 'ca', 'mx', and 'us' in
the list we pass to the first add() call to highlight Canada, Mexico, and the
United States together. We then do the same for the countries in Central
America and South America.
Note, that map is interactive and you SHOULD hover a mouse over each country, 
to see its data
'''
# Export country map chart to svg-file. Class variable "wm" is a chart
wm = pygal.maps.world.World()
wm.title = 'North, Central, and South America'
wm.add('North America', ['ca', 'mx', 'us'])
wm.add('Central America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
wm.add('South America', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf',
                         'gy', 'pe', 'py', 'sr', 'uy', 've'])
# Create an .svg file containing the chart, which you can open in your browser.
wm.render_to_file('Projects\DataImport\chart_americas.svg')
''' 
#@@@@@@@@@@@@@@@@@ CREATE ONE MORE CHART @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
wm = pygal.maps.world.World()
wm.title = 'Populations of Countries in North America'
wm.add('North America', {'ca': 34126000, 'us': 309349000, 'mx': 113423000})
wm.render_to_file('Projects\DataImport\chart_americas_population.svg')
'''
