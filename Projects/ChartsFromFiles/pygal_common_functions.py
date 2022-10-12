# Module = pygal.i18n is old now. Use pygal_maps_world insted
#from pygal.i18n import COUNTRIES 
#See: https://stackoverflow.com/questions/35770931/why-cant-i-import-countries-from-pygal-i18n
#====================================================
# (To install module below run: "pip install pygal_maps_world")
from pygal_maps_world.i18n import COUNTRIES 
#====================================================
'''             Obtaining Two-Digit Country Codes
Before we can focus on mapping, we need to address one last aspect of
the data. The mapping tool in Pygal expects data in a particular format:
countries need to be provided as country codes and populations as values.
Several standardized sets of country codes are frequently used when working
with geopolitical data; the codes included in population_data.json are
three-letter codes, but Pygal uses two-letter codes. We need a way to find
the two-digit code from the country name.
Pygal's country codes are stored in a module called i18n, short for
internationalization. The dictionary COUNTRIES contains the two-letter country
codes as keys and the country names as values. To see these codes, import
the dictionary from the i18n module and print its keys and values:
'''
#=============================================================================
# Return the Pygal 2-digit country code for the given country. 
def get_country_code(country_name):
    for code, name in COUNTRIES.items():
        if  name == country_name: # if country found exit at once and return result
            return code
    # If the country wasn't found, return None.
    return None
#-----------------------------------------------------------------------------
'''                          TESTING
print(get_country_code('Andorra'))              # = ad
print(get_country_code('United Arab Emirates')) # = ae
print(get_country_code('Afghanistan'))          # = af
'''
#=============================================================================
