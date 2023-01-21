# list comprehension

# transforming list without list comprehention
names = ['jerome', 'lauryn', 'elias']

my_list = []

for name in names:
    my_list.append(len(name))

print(my_list) #prints [6, 6, 5]

# using list comprehension
# square brackets with return value first and then list that you want to modify
list_comprehension = [len(name) for name in names]

print(list_comprehension) # prints [6, 6, 5]

# you can also add conditional at the end

conditional_comprehension = [name for name in names if len(name) % 2 == 0]

print(conditional_comprehension) # prints ['jerome', 'lauryn']

# dictionary comprehension

squares = {num: num ** 2 for num in range(4)}

print(squares) #prints {0: 0, 1: 1, 2: 4, 3: 9}

# generator expression ()
# once looped through than the generator can not be looped anymore

gen_expression = (num for num in range(2))

print(gen_expression) # shows that it's a generator

for num in gen_expression:
    print(num) # prints current num

# now gen expression can not be used anymore
for num in gen_expression:
    print(num) # prints nothing
