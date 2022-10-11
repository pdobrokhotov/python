from random import choice
#=============================================
'''
RandomWalk class, which will make random decisions about which direction 
the walk should take. The class needs three attributes: one variable to 
store the number of points in the walk and two lists to store the x- and
y-coordinate values of each point in the walk.
We'll use only two methods for the RandomWalk class: the __init__()
method and fill_walk(), which will calculate the points in the walk. 
To make random decisions, we'll store possible choices in a list and
use choice() to decide which choice to use each time a decision is made.
Function choice() returns a random item from a list, tuple, or string
We then set the default number of points in a walk to 5000—large enough
to generate some interesting patterns but small enough to generate walks
quickly. Then we make two lists to hold the x- and y-values, and we
start each walk at point (0, 0).
'''
# A class to generate random walks. 
class RandomWalk():
    #=============================================================================
    # Initialize attributes of a walk.
    def __init__(self, num_points=5000): 
        self.num_points = num_points
        # All walks start at (0, 0). We'll add more values later  
        self.x_values = [0] # create x-list with one initial value = 0
        self.y_values = [0] # create y-list with one initial value = 0
    #=============================================================================
    # Calculate all the points in the walk. 
    def fill_walk(self):
        # Keep taking steps until the walk reaches the desired length.
        while len(self.x_values) < self.num_points:
            # Decide which direction to go and how far to go in that direction.
            # Function choice() returns a random item from a list, tuple, or string
            x_direction = choice([1, -1]) # chose randomly 1 for right movement or −1 for left
            x_distance  = choice([0, 1, 2, 3, 4])
            # Positive result for x_step moves us right, 
            # a negative result moves us left 
            # and 0 moves us vertically
            x_step      = x_direction * x_distance 
            y_direction = choice([1, -1])
            y_distance  = choice([0, 1, 2, 3, 4])
            # A positive result for y_step means move up, negative means move down, 
            # and 0 means move horizontally. If the value of both x_step and y_step 
            # are 0, the walk stops, but we continue the loop to prevent this
            y_step      = y_direction * y_distance
            # Reject moves that go nowhere.
            if x_step == 0 and y_step == 0:
                continue
            # Calculate the next x and y values by adding value to the last element
            # Index = [-1] points to the last element in list
            # Index = [-2] points to the previous element of the last element and etc 
            next_x = self.x_values[-1] + x_step 
            next_y = self.y_values[-1] + y_step
            # Add new calculated values to the according lists we have already
            self.x_values.append(next_x)
            self.y_values.append(next_y)
            '''
            To get the next x-value for our walk, we add the value in x_step to the
            last value stored in x_values and do the same for the y-values. 
            Once we have these values, we append them to x_values and y_values
            '''
            #=============================================================================