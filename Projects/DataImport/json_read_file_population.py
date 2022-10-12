import json
#=========================================================
# Load the file into a list. Note that this file represents
# a Python list of dictionaries!
filename = 'Projects\DataImport\JSON\population_data.json'
with open(filename) as f:
    # Convert the data into a format Python can work with
    pop_data = json.load(f) 
    
#-----------------------------------------------------------
# Print the 2010 population for each country.
# Each item is a dictionary with four key-value pairs, 
# and we store each dictionary in pop_dict.
for pop_dict in pop_data: # loop our list of dictionaries
    #Do a string comparison, 'cause the values are in quotes
    if  pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        print(country_name + ": " + str(population))
#-----------------------------------------------------------

        