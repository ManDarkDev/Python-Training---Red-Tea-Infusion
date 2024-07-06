import math, sys # Imports the math and sys modules
print(dir()) # Prints a list of names in the current local scope
print(dir(__builtins__)) # Prints a list of all built-in names

print('#' * 50)# Prints a line of 50 hash (#) characters
print(dir(print)) # Prints a list of attributes and methods of the print function
print(__doc__) # Prints the docstring of the current module (if there is one)
help(print)# Shows the help documentation for the print function

print('#' * 50)# Prints a line of 50 hash (#) characters
print(list.append.__doc__) # Prints the docstring for the append method of list
help(list.append)

print('#' *50) # Prints a line of 50 hash (#) characters
print(dir(math)) # Shows the help documentation for the append method of list
print(math.log.__doc__)# Prints the docstring for the log function of the math module

print('#' * 50)# Prints a line of 50 hash (#) characters
print(sorted(set(filter(lambda x: not x.startswith('_'), sys.stdlib_module_names))))
# does not work in this .vscode terminal but works in Python terminal. Prints a sorted list of standard library module names excluding those that start with an underscore.
print(filter.__doc__) # Prints the docstring for the filter function. 

