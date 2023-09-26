'''
This is meant to test the functionality of a Car class. The class is
supposed to have the following attributes:

color : The color of the car (string)
cartype : The type of car, for example van, pickup, sedan, hatchback. (string)
hp : The horsepower of the engine (int)
running : Is the engine running? (bool)
pos : Position. x- and y-coordinate. Should be a dictionary of x (int) and y (int)

The class is supposed to have the following methods:

Start() : Turns the "running" attribute to True
Stop() : Turns the "running" attribute to False
DriveTo(x,y) : Sets the position to x, y IF car is running
GetPos() : Returns the position of the car
'''

import Car # <- Change if your filename differs

# Initiating empty object
myCar = Car()

print(f"Testing if printable.")
try:
    print(f"Empty car:\n{myCar}")
except:
    print("! Can not print the whole object !")


# Trying to access attributes
print("Setting attributes.")
try:
    myCar.color = "red"
    myCar.cartype = "pickup"
    myCar.hp = 290
    myCar.position['x'] = 0
    myCar.position['y'] = 0
    print("Attributes set.")
except:
    print("! Could not set attributes !")
 
print(f"Printing again.")
try:
    print(f"My car:\n{myCar}")
except:
    print("! Can not print the whole object !")
    print("Printing attributes instead.")
    print(f"Color: {myCar.color}")
    print(f"Type: {myCar.cartype}")
    print(f"Horsepower: {myCar.hp}")


# Testing methods
if myCar.running:
    print(f"The engine is running and the position is {myCar.GetPos()}")
else:
    print(f"The engine is not running and the position is {myCar.GetPos()}")

print("\nTesting methods:\n")
print("Driving to x=50, y=50.")
myCar.DriveTo(50, 50)
print(f"Position is {myCar.GetPos()}")
myCar.Start()
print("Driving to x=100, y=100.")
myCar.DriveTo(100, 100)
print(f"Position is {myCar.GetPos()}")
print("Turning engine off.")
myCar.Stop()


# Initiating a car, trying to set color, cartype and horsepower in creation.
print("\nInitiating a new car with attributes.")
newCar = Car(color = 'black', cartype = 'sportscar', hp = 600)

print(f"Printing new car.")
try:
    print(f"New car:\n{newCar}")
except:
    print("! Could not print whole car object !")
    print("Printing attributes instead.")
    print(f"Color: {myCar.color}")
    print(f"Type: {myCar.cartype}")
    print(f"Horsepower: {myCar.hp}")
    
print(f"Also testing docstring:\n{newCar.__doc__}")