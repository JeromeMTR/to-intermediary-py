# functions in python
# syntax required for func
# def key word telling python it's declaring a func
# name for func
# () opening and closing paranthesis
# optional args seperated with a comma inside paranthesis
# colon

# basic func that takes no args and returns nothing``
def hello_world():
    print('hello world!')

# func that takes two args and returns added val
def add_nums(x, y):
    return x + y

#args

#using default args
def say_greetings(name, greeting='Hi', punctuation='!!!'):
    print(f"{greeting}, {name}{punctuation}")

say_greetings('jerome')
#prints Hi, jerome!!!

say_greetings('jerome', 'whats up', '!')
#prints whats up, jerome!

#args without defaults are required'
def say_greeting(name, greeting):
    print(f"{greeting}, {name}.")

say_greeting("Nina")
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: say_greeting() missing 1 required positional argument: 'greeting'


