'''Lesson 24 - Enumerate
enumerate()'''
#Iterating Over a String
s = 'House.of.Python'
for index, element in enumerate(s): # Uses enumerate to get both index and element from the string 's'
    print(f'index = {index}, element = {element}')
# Iterating Over a List 
l = ['a,' 'b,' 'c,' 'd']
for index, element in enumerate(l[3:], start = 3): # Uses enumerate to get index and element, starting from index 3, for the slice l[3:]
    print(f'index+{index}, element ={element}')
# Iterating Over a Dictionary
d = {'a' : 1, 'b' : 2, 'c' : 3}
for index, (key, value) in enumerate(d.items()): # Uses enumerate to get index and (key, value) pairs from the dictionary 'd'
    print(f'index = {index}, key = {key}, value = {value}') 