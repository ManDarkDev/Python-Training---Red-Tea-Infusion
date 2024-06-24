numbers = [x for x in range (5)]# Creates a list of numbers from 0 to 4 using a list comprehension
print(numbers)# Prints the list of numbers [0, 1, 2, 3, 4]

squares = [x**2 for x in range (5)]  # (order: 0^2, 1^2, 2^2, 3^2, 4^2 -> 0, 1, 4, 9, 16)
print(squares)

double_even = [x*2 for x in numbers if x % 2 == 0] #(order: 0*2, 2*2, 4*2 -> 0, 4, 8)
print(double_even)

matrix = [numbers for x in range(3)]# Creates a 3x5 matrix where each row is the 'numbers' list (each row: 0, 1, 2, 3, 4)
print(matrix)

# the syntax will list matrix of numbers horizontally with no new line
matrix2 = [[x for x in range(5)] for y in range(3)]
print(matrix2) 

  #OR

# this syntax will list matrix vertically
matrix2 = [[x for x in range (5)]] # Creates a 3x5 matrix with each row containing numbers from 0 to 4 (each row: 0, 1, 2, 3, 4)
for y in range(3):# indentation seems to print the single row vertically
    print(matrix2)

  