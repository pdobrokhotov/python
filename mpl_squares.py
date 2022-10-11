import matplotlib.pyplot as plt # renders chart on scree that you can play with
'''
Let''s plot a simple line graph using matplotlib, and then customize it to
create a more informative visualization of our data. We'll use the square
number sequence 1, 4, 9, 16, 25 as the data for the graph. Just provide 
matplotlib with the numbers as shown here, and matplotlib should do the rest:
'''
# We create a list to hold the squares and then pass it to the plot() function,
# which will try to plot the numbers in a meaningful way. Function plt.show()
# opens matplotlib’s viewer and displays the plot 
input_values = [1, 2, 3, 4, 5] # x-values
squares = [1, 4, 9, 16, 25]    # y-values (manual)
# squares = [value**2 for value in input_values] # here we calculate values automatically

# Tune our chart!
plt.plot(input_values, squares, linewidth=5) # put lists on axises
# Set chart title and label axes.
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
# Set size of tick labels. The arguments shown here affect the tick marks 
# on both the x- and y-axes (axes='both') and set the font size of the tick 
# mark labels to 14 (labelsize=14).
plt.tick_params(axis='both', labelsize=14) 
# Show plot on screen
plt.show()

