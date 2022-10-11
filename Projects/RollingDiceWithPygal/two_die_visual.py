# Import this Main library for coding that allows saving resulted chart
# to a picture-file, thatis interactive when opend in browser
import pygal 
#Import our Die-сlass (Кубик с 6 сторонами по умолчанию)
from die import Die 
'''
After creating two instances of Die, we roll the dice and calculate
the sum of the two dice for each roll. The largest possible result (12) 
is the sum of the largest number on both dice, which we store in max_result.
The smallest possible result (2) is the sum of the smallest number on both
dice. When we analyze the results, we count the number of results for each
value between 2 and max_result. (We could have used range(2, 13), but
this would work only for two D6 dice. When modeling real-world situations,
it's best to write code that can easily model a variety of situations. This code
allows us to simulate rolling a pair of dice with any number of sides.)
When creating the chart, we update the title and the labels for the x-axis
and data series x. (If the list x_labels were much longer, it would make sense
to write a loop to generate this list automatically.)
As we see, when usinf 2 D6-dices the most popular sum of 2 dice = 7 !!!!
because there are six ways to roll a 7, namely: 1 and 6, 2 and 5, 3 
and 4, 4 and 3, 5 and 2, or 6 and 1.
'''


#=====================================================
# Create two D6 dice.
die_1 = Die()
die_2 = Die()

# Create empty list and store there our random die's results for 1000 attempts
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)
#------------------------------------------------------------------------
# Analyze the results.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides

for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)
#print("====================== FREQUENCY ============================")
#print(frequencies)
#====================================================================
# Visualize the results.
hist = pygal.Bar()
# Tune chart
hist.title = "Results of rolling two D6 dice 1000 times."
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']

hist.x_title = "Result"
hist.y_title = "Frequency of Result"
# Add a series of values to the chart
hist.add('D6 + D6', frequencies)
# Save resulted chart to file, which expects a filename 
# with the .svg extension. Notice that Pygal has made 
# the chart interactive: hover your cursor over any bar 
# in the chart and you’ll see the data associated with it. 
# This feature is particularly useful when plotting multiple 
# data sets on the same chart.
hist.render_to_file('Projects/RollingDiceWithPygal/two_die_visual.svg') 