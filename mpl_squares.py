import matplotlib.pyplot as plt
'''
Let''s plot a simple line graph using matplotlib, and then customize it to
create a more informative visualization of our data. We'll use the square
number sequence 1, 4, 9, 16, 25 as the data for the graph. Just provide 
matplotlib with the numbers as shown here, and matplotlib should do the rest:
'''
# We create a list to hold the squares and then pass it to the plot() function,
# which will try to plot the numbers in a meaningful way. Function plt.show()
# opens matplotlib’s viewer and displays the plot 
squares = [1, 4, 9, 16, 25]
plt.plot(squares)
plt.show()