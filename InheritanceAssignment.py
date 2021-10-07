# Here im defining a parent class with its properties and using a printname method.
class Bikes:
    #function to give structure to objects in the class Bikes
    def __init__(self, type_of, color):
        self.type_of = type_of
        self.color = color

    #function for defining structure of the printname method for printing
        #the attrubutes of a bike(object) in class Bikes
    def printname(self):
        print(self.type_of, self.color)

# using the Bikes class to create an object, and then executing the printname method:

x = Bikes("Mountain", "Mustard-Yellow")
x.printname()


# Here creating child class ElectricBike with its own attributes
class ElectricBike(Bikes):
    engine = 'Dual-Battery'
    battery_energy = '500 wh'
    load = '250w'
    run_time = '2 hours'



#a 2nd child class MotorBike
class MotorBike(Bikes):
    speed = '90 mph'
    to_decrease = 'brake lever'
