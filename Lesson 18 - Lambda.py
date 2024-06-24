add = lambda x: x+1 # Defines a lambda function to add 1 to the input
print(add(3)) # Prints the result of calling the lambda with 3 (Output: 4)

add_numbers = lambda x, y: x + y # Defines a lambda function to add two numbers
print(add_numbers(4, 5))# Prints the result of calling the lambda with 4 and 5 (Output: 9)

letters = ['yyyy' , 'zzz' , 'aaaaa', 'xxxxx', 'wwwwww']# List of strings
print(letters)
letters.sort(key = lambda x: len(x))# Sorts the list by string length using a lambda function
print(letters)

def add_one(n): # Defines a function that returns a lambda adding 'n' to its input
    return lambda x: x + n # Lambda function to add 'n' to 'x'
number = add_one(20)# 'number' is now a lambda that adds 20 to its input
print(number(1))# Prints the result of calling this lambda with 1 (Output: 21)