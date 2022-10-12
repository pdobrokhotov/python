# python
ALL THE EXAMPLES IN THIS REPO WERE TAKEN FROM BOOK
https://www.booksfree.org/python-crash-course-by-eric-matthes-pdf-free-download/
------------------------------------
Installing matplotlib library 
pip install matplotlib
NOTES:
1) see https://pypi.python.org/
2) see https://matplotlib.org/
   When you click a visualization in the gallery, you can see the code 
   used to generate the plot
------------------------------------
Installing pygal library 
python -m pip install --user pygal
NOTES:
1)You may need to use the command pip3 instead of pip, and if the command  
still doesn’t work you may need to leave off the --user flag.
2) To see what kind of visualizations are possible with Pygal, visit the gallery of
chart types: go to http://www.pygal.org/, click Documentation, and then click
Chart types. Each example includes source code, so you can see how the
visualizations are generated.
------------------------------------
Country List module of PYGAL
To install it run: "pip install pygal_maps_world"
After install use it like shown below:
from pygal_maps_world.i18n import COUNTRIES 
for country_code in sorted(COUNTRIES.keys()):
    print(country_code, COUNTRIES[country_code])
------------------------------------
Country Map module of PYGAL
To install it run: "pip install pygal_maps_world"
After install use it like shown below:
import pygal
mm = pygal.maps.world.World()
------------------------------------
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




