def my_function(): # Defines a function named my_function
    print('Hello World')

def greet(name = 'World'):# Defines a function named greet with a default parameter name ='World'
    print('Hello', name)

def add(a,b = 3):# Defines a function named add with parameters a and b, where b has a default value of 3
    return a + b
def add_args(*args):# Defines a function named add_args that takes a variable number of arguments
    result = 0
    for n in args:
        result += n 
    return result
    
my_function()# Calls my_function, which prints 'Hello World'
greet('Red') # Calls greet with the argument 'Red', which prints 'Hello Red'
greet()# Calls greet with no arguments, which prints 'Hello World' (using the default parameter value)
number = add(2)# Calls add with the argument 2, returns 2 + 3 (default b) and assigns the result to number
print(number)# Prints the value of number
print(add_args(1, 2, 3, 4, 5, 6)) # Calls add_args with multiple arguments, returns their sum, and prints the result