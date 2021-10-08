# Parent class
class Predator:
    name = "Jaguar"
    size = "Medium"
    position = "Apex Predator"


# Here is the function that will be utilized as polymorphism for the child classes below
    def disp(self):
       entry_name = input("Enter its name: ")
       entry_size = input("Enter its size: ")
       entry_position = input("Enter Position in Food Chain: ")
       #this if statement provides an input function requiring it's arguments
       # as it prints an welcome message and error message
       if (entry_size == self.size and entry_position == self.position):
           print("Welcome to the Food Chain, {}!".format(entry_name))
       else:
           print("This being doesn\'t belong in the Food Chain.")
            

#child class instance
class Prey(Predator):
    #super() function takes place of parent class name to
        #inherit automatically all methods and properties from its parent
    food = 'Insects and crumbs of food'
    weight = '2.3 lbs'
    food_required = 'Insects'

# this is the same method in the parent class "Predator".
#the difference is, instead of using entry_position, i'm using entry_food.
    def disp(self):
        entry_name = input("Enter its name: ")
        entry_size = input("Enter its size: ")
        entry_food = input("Enter food required in Food Chain: ")
       #this if statement provides an input function requiring it's arguments
       # as it prints an welcome message and error message
        if (entry_size == self.size and entry_food == self.food_required):
           print("Welcome to the Food Chain, {}!".format(entry_name))
        else:
           print("This food doesn\'t belong in the Food Chain.")

#another child class instance
class Producer(Predator):
        #super() function takes place of parent class name to
        #inherit automatically all methods and properties from its parent
    type_of = 'Grass'
    provides = 'Oxygen'
    whats_provided = 'Oxygen'

# this is the same method in the parent class "Predator".
#the difference is, instead of using entry_position, i'm using entry_food.
    def disp(self):
        entry_name = input("Enter its name: ")
        entry_size = input("Enter its size: ")
        entry_provides = input("Enter what's provided by the producer: ")
       #this if statement provides an input function requiring it's arguments
       # as it prints an welcome message and error message
        if (entry_size == self.size and entry_provides == self.whats_provided):
           print("Welcome to the Food Chain, {}!".format(entry_name))
        else:
           print("This product doesn\'t belong in the Food Chain.")

# the following code invokes the methods inside each class for parent and child classes
predator = Predator()
predator.disp()

prey = Prey()
prey.disp()

producer = Producer()
producer.disp()
