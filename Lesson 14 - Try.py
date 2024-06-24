try :# Start of the try block to catch exceptions
    print(10/0)# Attempts to print the result of 10 divided by 0, which will cause an exception
except Exception as e: # If an exception occurs, it is caught here
    print(e) # Prints the exception message ('division by zero')
    # pass
print('Program terminated')# Prints 'Program terminated' regardless of exceptions

try:
    i = input ('Insert a number: ')# Prompts the user to input a number
    i = int(i)# Attempts to convert the input to an integer
    print(i)
    print(10/i)
except ValueError:
     print(i, 'is not a number')
except ZeroDivisionError:
    print('i can\'t be 0')
else: 
    print('I print if there aren\'t errors')
finally:
    print('I print always')