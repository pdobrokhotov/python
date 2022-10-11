# Import this Main library for coding that allows saving resulted chart
# to a picture-file, thatis interactive when opend in browser
import pygal 
#Import our Die-сlass (Кубик с 6 сторонами по умолчанию)
from die import Die 
#=====================================================
# Create a D6-die (default) 
die = Die()
# Create empty list and store there our random die's results for 1000 attempts
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)
# print(results)
#------------------------------------------------------------------------
# Analyze the results.
frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)
#print("====================== FREQUENCY ============================")
#print(frequencies)
#====================================================================
# Visualize the results.
hist = pygal.Bar()
# Tune chart
hist.title = "Results of rolling one D6 1000 times."
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
# Add a series of values to the chart
hist.add('D6', frequencies) 
# Save resulted chart to file, which expects a filename 
# with the .svg extension. Notice that Pygal has made 
# the chart interactive: hover your cursor over any bar 
# in the chart and you’ll see the data associated with it. 
# This feature is particularly useful when plotting multiple 
# data sets on the same chart.
hist.render_to_file('Projects/RollingDiceWithPygal/die_visual.svg') 