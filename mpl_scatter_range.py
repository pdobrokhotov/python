import matplotlib.pyplot as plt
#=================================================
# plot a simple point. 
# plt.scatter(2, 4, s=200) # x=2, y=4, size=200
#=================================================
# Plot several points in list
x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]
'''
matplotlib lets you color points individually in a scatter plot. The default—
blue dots with a black outline—works well for plots with a few points. But
when plotting many points, the black outlines can blend together. To
remove the outlines around points, pass the argument edgecolor='none'
when you call scatter().In this you'll see only solid blue points in your plot.
We can use custom color: c=(0, 0, 0.8). Values closer to 0 produce dark colors, 
and values closer to 1 produce lighter colors.
'''
plt.scatter(x_values, 
            y_values, 
            c='red',          # color. We can use custom color as RGB(): c=(0, 0, 0.8)
                              # Values closer to 0 produce dark colors 
                              # values closer to 1 produce lighter colors
            edgecolor='none', # edging
            s=40)             # size

# Set chart title and label axes.
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
# Set size of tick labels.
plt.tick_params(axis='both', which='major', labelsize=14)
# Set the range for each axis. The axis() function requires 
# four values: the minimum and maximum values for the x-axis 
# and the y-axis. Here, we run the x-axis from 0 to 1100 
# and the y-axis from 0 to 1,100,000.
plt.axis([0, 1100, 0, 1100000])

# Show chart
plt.show()
# Save chart as file in the same folder where the code file is placed. 
# The first argument is a filename for the plot image, which will be saved
# in the same directory as scatter_squares.py. The second argument trims extra
# whitespace from the plot. If you want the extra whitespace around the plot,
# you can omit this argument.
#plt.savefig('squares_plot.png', bbox_inches='tight')