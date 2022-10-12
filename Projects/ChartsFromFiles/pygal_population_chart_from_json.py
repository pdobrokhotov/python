import json
import pygal
# that allows to use smarter colors 
from pygal.style import LightColorizedStyle as LCS, RotateStyle as RS
# Import our function that we defined
from pygal_common_functions import get_country_code
#=========================================================
# Load the file into a list. Note that this file represents
# a Python list of dictionaries!
filename = 'Projects\DataImport\JSON\population_data.json'
with open(filename) as f:
    # Convert the data into a format Python can work with
    pop_data = json.load(f) 
#-----------------------------------------------------------
# Create a dictionary for population data. We'll fill it later
country_plus_population_pair = {}    
#-----------------------------------------------------------
# Print the 2010 population for each country.
# Each item is a dictionary with four key-value pairs, 
# and we store each dictionary in pop_dict.
for pop_dict in pop_data: # loop our list of dictionaries
    #Do a string comparison, 'cause the values are in quotes
    if  pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        # print(country_name + ": " + str(population))
        # Get 2-chars country code by its name using our imported function
        code = get_country_code(country_name)
        if code:
            #print(code + ": "+ str(population))
            country_plus_population_pair[code] = population
        else:
            #print('ERROR - ' + country_name)
            continue
#========================================================================== 
# Group the countries into 3 population levels.
# Thus, create an empty dictionary for each category
cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
# The if-elif-else block adds an entry to the appropriate dictionary
for cc, pop in country_plus_population_pair.items():
    if pop < 10000000:
        cc_pops_1[cc] = pop
    elif pop < 1000000000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop
#------------------------------------------------------------------------
# See how many countries are in each level.
# print(len(cc_pops_1), len(cc_pops_2), len(cc_pops_3)) # = 85, 69, 2
#============== RENDER CHART TO FILE ====================================
# Craete an empty world chart, tune it and fill with data
# Also apply styling for smarter coloring (not required but preferred)
# RotateStyle-class takes one argument, an RGB color in hex format.
# Pygal then chooses colors for each of the groups based on it
# The simplest way to do this os shown in commented line below
#        wm_style = RotateStyle('#336699') # pass RGB-code to class
# But here we use advanced styling, though I do not see any difference
wm_style = RS('#336699', base_style=LCS) # pass RGB-code to class
wm = pygal.maps.world.World(style= wm_style) # chart uses Style provided
'''
The hex format is a string with a hash mark (#) followed by
six characters: the first two represent the red component of the color, the
next two represent the green component, and the last two represent the
blue component. The component values can range from 00 (none of that
color) to FF (maximum amount of that color). If you search online for hex
color chooser, you should find a tool that will let you experiment with colors
and give you the RGB values. The color used here (#336699) mixes a bit
of red (33), a little more green (66), and even more blue (99) to give
RotateStyle a light blue base color to work from. RotateStyle returns a 
style object, which we store in wm_style. To use this style object, pass 
it as a keyword argument when you make an instance of Worldmap.
This styling gives the map a unified look, and it results in groups that
are easy to distinguish.
''' 
#-------------------------------------------------------------------------
# Set Char Title
wm.title = 'World Population in 2010, by Country'
# Make sure to add all three groups to the Worldmap
# Note that each time we add a list, it gets new color
wm.add('0-10m', cc_pops_1)
wm.add('10m-1bn', cc_pops_2)
wm.add('>1bn', cc_pops_3)  
# Save rsultes chart to a file that is interactive in browser          
wm.render_to_file('Projects\DataImport\chart_world_population_from_json.svg')

       