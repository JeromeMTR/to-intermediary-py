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

# say_greeting("Nina")
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: say_greeting() missing 1 required positional argument: 'greeting'

# boolean logic

def check_equality(x, y):
    print(x == y)

check_equality(1, 1) #prints true

# with arrays it checks if the content is the same not the address
check_equality([2], []) #prints false
check_equality([1, 3, 5], [1, 3, 5]) # prints true

# checks is the same object in memory
def is_identical(x, y):
    print('same object in memory?',x is y)

letter = 'a'
other_letter = 'a'

array_1 = [1, 2, 4]

is_identical(letter, other_letter) #prints true
is_identical(array_1, [1, 2, 4]) #prints false
is_identical(array_1, array_1) #prints true


def is_not_identical(x, y):
    print('is not the same object in memory?', x is not y)

is_not_identical(letter, other_letter) #prints false
is_not_identical(array_1, [1, 2, 4]) #prints true
is_not_identical(array_1, array_1) #prints false









