# tuples ()
# tuples are immutable, once created; items can not change
# you can not add, remove, or update like a list

subjects = ('math', 'english', 'history', 1, 2, 3)

#accessing elements in tuple
math = subjects[0]
print(math) # prints math in console

subjects[0] = 'science'
# Traceback (most recent call last):
#   File "<stdin>", line 11, in <module>
# TypeError: 'tuple' object does not support item assignment

#tuple unpacking
period1, period2, period3, one, two, three = subjects

print(period1) #prints math
print(period2) #prints math
print(period3) #prints math
