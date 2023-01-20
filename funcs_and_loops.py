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


# loops
# combines in keyword and for keyword can be used to indicate loping over each item in a sequence

colors = ['red', 'yellow', 'green']

for color in colors:
    print(f"the current color is {color}")

# prints the current color is red
# prints the current color is yellow
# prints the current color is green


# looping over range of numbers
# you can use the builtin function range()

for num in range(5):
    print(num)

# prints 0
# prints 1
# prints 2
# prints 3
# prints 4

# what if we wanted 2 through 4
for num in range(2, 5):
    print(num)

# prints 2
# prints 3
# prints 4

# what if we wanted both the index and the val
# use enumerate to turn it in to a tuple and unpackage it

for index, color in enumerate(colors):
    print(f"the index is {index}, and the color is {color}")

# prints the index is 0, and the color is red
# prints the index is 1, and the color is yellow
# prints the index is 2, and the color is green

# what would be the time complexity of enumerate and a for loop????


# looping over dictionaries
nums = {
    'one': 111,
    'two': 222,
}

for key in nums:
    print(f'the current key is {key}')

# prints the current key is one
# prints the current key is two

# when looping to get the val and key, use dict.items()
for key, value in nums.items():
    print(f'the current key is {key}, and the value is {value}')
