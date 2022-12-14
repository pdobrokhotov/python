class Dog():
    """A simple attempt to model a dog."""
    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age
    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(self.name.title() + " is now sitting.")
    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(self.name.title() + " rolled over!")
#====================================================================================
'''
my_dog = Dog('willie', 6)
your_dog = Dog('lucy', 3)
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
my_dog.sit()
print("\nYour dog's name is " + your_dog.name.title() + ".")
print("Your dog is " + str(your_dog.age) + " years old.")
your_dog.sit()
'''

#======================================================================================
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
'''  
my_new_car = Car('audi', 'a4', 2016)
my_new_car.set_mileage(23)
# my_new_car.set_mileage(2)
print(my_new_car.get_descriptive_name())
print(my_new_car.show_mileage())
my_new_car.increment_mileage(2)
print(my_new_car.show_mileage())
''' 
#================== Inherited (child) class =============================== 
#At u we start with Car. When you create a child class, the parent class must 
#be part of the current file and must appear before the child class in the file.
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
        
                   
#=========================================================================        
my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.set_gas_amount() # this call overides a method from parent class = Car
#print(my_tesla.battery_charge)
my_tesla.show_battery_charge()
my_tesla.battery.show_battery_charge()



