# Everything in python is an ojbect...
# functions, variables, a property, a class

# classes
# for ex:
# number 42 is an instance of the class int
# string 'hello, world' is an instance of the str class

# oop is structured around classes and instances

# just like a car is a class but a toyota can be an instance of that class

class Car:
    runs = True

    def start(self):
        if self.runs:
            print('vrooom your car has started')
        else:
            print('car broken, tow it to the shop')

toyota_car = Car() # creates instance of class
print(f"does the toyota run: {toyota_car.runs}") # should be true

toyota_car.start() #prints vroom your car has started

# you can create multiple instances of the car class that keeps track of default values set and changes only to that instance

honda_car = Car()
honda_car.runs = False
honda_car.start() # prints car broken, tow it to the shop


# Methods in class and custom instantiation

class Vehicle:

    wheels = 4

    def __init__(self, wheels=4):
        self.runs = True
        self.wheels = wheels

    @classmethod
    def get_default_wheels(cls):
        ''' gets default wheels '''
        return cls.wheels

    def start(self):
        if self.runs:
            print('vehicle is working')
        else:
            print('vehicle needs some maitence')

bike = Vehicle(2)
print(bike.get_default_wheels()) # prints class defualt wheels
print(bike.wheels) # prints current instantiantion wheels

