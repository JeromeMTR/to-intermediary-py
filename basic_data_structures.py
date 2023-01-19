# tuples ()
# tuples are immutable, once created; items can not change
# you can not add, remove, or update like a list

subjects = ('math', 'english', 'history', 1, 2, 3)

#accessing elements in tuple
math = subjects[0]
print(math) # prints math in console

# subjects[0] = 'science'
# Traceback (most recent call last):
#   File "<stdin>", line 11, in <module>
# TypeError: 'tuple' object does not support item assignment

#tuple unpacking
period1, period2, period3, one, two, three = subjects

print(period1) #prints math
print(period2) #prints math
print(period3) #prints math

# sets {}
# only allow you to store immutable tyupes in an unsorted way
# they can be mutable; add or remove from sets
# sets do not include duplicates and stores only one instace of a unique item

# declaring empty set must use keyword set
my_new_set = {}
print(type(my_new_set)) # prints <class 'dict'>

actual_empty_set = set()
print(type(actual_empty_set)) # prints <class 'set'>

# contains no duplicates
nums = {2, 3, 3, 4, 4, 4}
print(nums) # prints {2, 3, 4}

# can be used to de duplicate
names = ['jerome', 'jerome', 'jerome', 'lauryn', 'lauryn']
unique_names = set(names)
print(unique_names) #prints ['jerome', 'lauryn']

# dicts or dictionaries
# are used to store data in key, value pairs.
# dicts are mutable but the keys have to be immutable types

my_dict = {}
print(type(my_dict)) #prints <class 'dict'>

new_dict = dict()
print(type(new_dict)) #prints <class 'dict'>

# creating key value pairs
numbers = {
    1: 'one',
    3: 'three',
    5: 'five'
}

print(len(numbers)) #prints 3

#accessing dicts
order = {
    'menu1': 'shrimp',
    'menu2': 'beef'
}

print(order['menu1']) #prints shrimp

# useful methods with dict
print(order.keys()) # prints dict_keys(['menu1', 'menu2'])
print(order.values()) # prints dict_values(['shrimp', 'beef'])
print(order.items()) # prints dict_items([('menu1', 'shrimp'), ('menu2', 'beef')])
