#======================================================================================
# NOTE: When we use "self"-prefix with variable, it means this variable can be accesed with CLASS
class Car():
    """A simple attempt to represent a car."""
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.mileage = 0    # we d0 not pass value for this, but can read\edit this value
        self.gas_amount = 0 # stores gas amount
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    def show_mileage(self):
        """Print a statement showing the car's mileage."""
        print("This car has " + str(self.mileage) + " miles on it.")
        #return self.mileage
    def set_mileage(self, mileage):
        #Reject the change if it attempts to roll the odometer back.
        if mileage >= self.mileage:
           self.mileage = mileage
        else:
           print("You can't roll back an mileage!")
    def increment_mileage (self, miles):
        """Add the given amount to the odometer reading."""
        self.mileage += miles  
    def set_gas_amount (self, gas_amount):
        """increments gas"""
        self.gas_amount += gas_amount          
#======================== LITTLE BATTERY CLASS WE'LL USE AS ATTRIBUTE =================
class Battery(): # A simple attempt to model a battery for an electric car 
    def __init__(self, battery_charge=70):
        self.battery_charge = battery_charge
    def show_battery_charge(self):
        print("This car has a " + str(self.battery_charge) + "-kWh battery.")    
#====================================================================================== 
class ElectricCar(Car):
    """Represent aspects of a Car-class, specific to electric vehicles."""
    def __init__(self, make, model, year): #Initialize attributes of the parent class. 
        super().__init__(make, model, year) # call the __init__() method from parent class = Car
        self.battery_charge = 70 # special property(attribute) that belongs to this child class ONLY
        self.battery = Battery() # attribute can be a class itself! Thus,instead of line above 
                                 # we use another class as an atribute for this class
    def show_battery_charge(self):        #Print a statement describing the battery size. 
        #print("This car has a " + str(self.battery_charge) + "-kWh battery charge.") 
        self.battery.show_battery_charge() # instead of line above we use class-varible 
    def set_gas_amount (self): # this method taken from parent class is overiden 
        print("This car doesn't have a gas tank!")   
        
#============================================================================
#====== The class below wil'be use for TESTING in [TESTING_CLASS.py] ======== 
#============================================================================
# This CLASS collects anonymous answers to a survey question. 
'''
This class starts with a survey question that you provide and includes
an empty list to store responses. The class has methods to print the survey
question, add a new response to the response list, and print all the
responses stored in the list x. To create an instance from this class, 
all you have to provide is a question. Once you have an instance representing
a particular survey, you display the survey question with show_question(), 
store a response using store_response(), and show results with show_results().
'''
class AnonymousSurvey(): 
    def __init__(self, question): # Store a question, and prepare to store responses. 
        self.question = question
        self.responses = []
    def show_question(self): # Show the survey question. 
        print(self.question)
    def store_response(self, new_response): # Store a single response to the survey. 
        self.responses.append(new_response)
    def show_results(self): # Show all the responses that have been given. 
        print("Survey results:")
        for response in self.responses:
            print('- ' + response)
#============================================================================



