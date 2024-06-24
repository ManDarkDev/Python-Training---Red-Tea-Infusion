lessons = {'Lesson 01': 'String', 'Lesson 02': 'Variable'}# - Creates a dictionary with lesson titles and topics
print(type(lessons), lessons)# Prints the type and content of the lessons dictionary
print(lessons['Lesson 01'])# Prints the value associated with the key 'Lesson 01'
print(lessons.keys())# Prints all the keys in the lessons dictionary
print(lessons.values()) # Prints all the values in the lessons dictionary
lessons['Lesson 03'] = 'Integer'# - adds a new key-value pair to the lessons dictionary
print(lessons)

for key in lessons:
    print('key =', key, ' value =', lessons[key])

    for i in range (len(lessons)):
        print(list(lessons.values())[i])

#ALTERNATIVE CODE

lessons = {'Lesson 01': 'String', 'Lesson 02': 'Variable'} # Creates a dictionary with lesson titles and topics
print(type(lessons), lessons) # Prints the type and content of the lessons dictionary
print(lessons['Lesson 01']) # Prints the value associated with the key 'Lesson 01'
print(lessons.keys()) # Prints all the keys in the lessons dictionary
print(lessons.values()) # Prints all the values in the lessons dictionary

lessons['Lesson 03'] = 'Integer' # Adds a new key-value pair to the lessons dictionary
print(lessons)

keys_to_delete = []
for key in lessons:  # Iterates over each key in the lessons dictionary
    print('key =', key, ' value =', lessons[key])  # Prints the key and its corresponding value
    if key == 'Lesson 03':
        keys_to_delete.append(key)  # Collects keys to delete

for key in keys_to_delete:  # Safely deletes collected keys after iteration
    del lessons[key]  # Deletes the key-value pair

for i in range(len(lessons)):  # Iterates over the indices of the values in the lessons dictionary
    print(list(lessons.values())[i])  # Converts the dictionary values to a list and prints each value by index







