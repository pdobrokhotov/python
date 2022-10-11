import matplotlib.pyplot as plt
#=================================================
# plot a simple point. 
# plt.scatter(2, 4, s=200) # x=2, y=4, size=200
#=================================================
# Plot several points in list
# The points to be plotted are (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)
x_values = [1, 2, 3, 4, 5]
# y_values = [1, 4, 9, 16, 25]      # here we set values manually 
y_values = [x**2 for x in x_values] # here we calculate values automatically
'''
matplotlib lets you color points individually in a scatter plot. The default—
blue dots with a black outline—works well for plots with a few points. But
when plotting many points, the black outlines can blend together. To
remove the outlines around points, pass the argument edgecolor='none'
when you call scatter(). In this you'll see only solid blue points in your plot.
plt.scatter(x_values, y_values, edgecolor='none', s=40)
'''
plt.scatter(x_values, y_values, s=100)
# Set chart title and label axes.
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
# Set size of tick labels.
plt.tick_params(axis='both', which='major', labelsize=14)
# Set the range for each axis if needed
# plt.axis([1, 10, 1, 30])

# Show chart
plt.show()
# Save chart as file in the same folder where the code file is placed. 
# The first argument is a filename for the plot image, which will be saved
# in the same directory as scatter_squares.py. The second argument trims extra
# whitespace from the plot. If you want the extra whitespace around the plot,
# you can omit this argument.
#plt.savefig('squares_plot.png', bbox_inches='tight')