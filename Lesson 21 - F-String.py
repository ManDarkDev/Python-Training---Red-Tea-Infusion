s = 'python'
print(f'{s.title()}')# ".title" capitalizes the P in python.

n1 = 1 
n2 = 2
print(f'{n1} + {n2} = {n1 + n2}') # integer F String, resulting in '1 + 2 = 3'

pi = 3.14159265
print(f'pi = {pi:.2f}') # Formats the value of pi to 2 decimal places, resulting in 'pi = 3.14'

print(f"n1 = {n1:010d}") # Formats n1 as a 10-digit integer with leading zeros, resulting in 'n1 = 0000000001'

print(f'{s.replace("p", "P")}\n'\
      f'It\'s {s}!')
