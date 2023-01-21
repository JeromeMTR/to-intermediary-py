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



