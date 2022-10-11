import matplotlib.pyplot as plt
from random_walk import RandomWalk
#============================================================================
'''
We'll use a colormap to show the order of the points in the walk and then
remove the black outline from each dot so the color of the dots will be
clearer. To color the points according to their position in the walk, we
pass the c argument a list containing the position of each point. Because
the points are plotted in order, the list just contains the numbers from 
1 to 5000
First we use range() to generate a list of numbers equal to the number
of points in the walk. Then we store them in the list point_numbers, which
we'll use to set the color of each point in the walk. We pass point_numbers to
the c argument, use the Blues colormap, and then pass edgecolor=none to get
rid of the black outline around each point. The result is a plot of the walk
that varies from light to dark blue along a gradient,
'''
#================================================================
# Keep making new walks, as long as the program is active.
while True:
    # Make a random walk, and plot the points.
    # rw = RandomWalk() # no params passed. 5000 points by default
    rw = RandomWalk(50000)
    rw.fill_walk()
    # Feed the walk's x- and y-values to scatter() and tune chart
    # To color the points according to their position in the walk, 
    # we pass the c argument a list containing the position of each point
    # Note, that num_points is stored in class and = 5000 by default
    # Because the points are plotted in order, the list just contains  
    # the numbers from 1 to 5000
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, # pass list for x-axis
                rw.y_values, # pass list for y-axis
                c=point_numbers, # Max num on which color map will be based (=5000)
                cmap=plt.cm.Blues, # Use automatic coloring depending on c-Value
                edgecolor='none', 
                s=1) # point size = 1 pixel
    # Also Emphasize the first and last points.
    # For this we call the same method again but rerender first\last points again
    plt.scatter(0, 0, 
                c='green', edgecolors='none', s=100) # Start point GREEN
    plt.scatter(rw.x_values[-1], rw.y_values[-1], 
                c='red', edgecolors='none',s=100)    # End point RED
    #----------------------------------------------------------------------------
    # Remove the axes if needed (this somehow does NOT work correctly!)
    # plt.axes().get_xaxis().set_visible(False)
    # plt.axes().get_yaxis().set_visible(False)
    #-----------------------------------------------------------------------------
    # Show tuned Chart
    plt.show()
    # Ask user if to continue
    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break