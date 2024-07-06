'''Lesson 29 - Annotation
annotation
__annotation__
__doc__
global'''
largest_area = 0 #Defines largest area as 0

def greet (name: str) -> str: # Define a function 'greet' that takes a string and returns a string
    '''Greetings Fellow Nerds of CyberSpace'''
    return f'Learning {name}'# Return a formatted string with the given name

def triangle_area(base: float, height: float) -> float:# Define a function to calculate the area of a triangle
      global largest_area # Use the global variable largest_area
      area: float = base * height / 2  # Calculate the area of the triangle
      if area > largest_area: # If the calculated area is larger than the current largest_area
         largest_area = area  # Update largest_area to the new larger area

      return area # Return the calculated area

def main():# Define the main function
         print(greet('Schematics'))# Call the greet function and print its return value
         print(greet.__annotations__)# Print the type annotations of the greet function
         print(greet.__doc__) # Print the docstring of the greet function

         print(triangle_area(7.0, 5))# Call the triangle_area function with base 7.0 and height 3.5, and print the result
         print(triangle_area.__annotations__)# Print the type annotations of the triangle_area function
         print(triangle_area(5,10)) # Call the triangle_area function with base 5 and height 10, and print the result
         print(largest_area) #input number for largest area before u print (shown at top line)
        
if __name__ == '__main__':# If this script is run directly (not imported as a module)
    main()# Call the main function
