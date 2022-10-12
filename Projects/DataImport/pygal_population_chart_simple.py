import pygal
#=========================================================
'''
First create a Worldmap instance and set a title. Then use the add()
method, but this time pass a dictionary as the second argument instead of
a list. The dictionary has Pygal two-letter country codes as its keys and
population numbers as its values. Pygal automatically uses these numbers to
shade the countries from light (least populated) to dark (most populated).
Note, that map is interactive and you SHOULD hover a mouse over each country, 
to see its data
'''
wm = pygal.maps.world.World()
wm.title = 'Populations of Countries in North America'
wm.add('North America', {'ca': 34126000, 'us': 309349000, 'mx': 113423000})
wm.render_to_file('Projects\DataImport\chart_americas_population.svg')
