#Lesson 09: Import command
#import: Loads external Python modules or libraries into a program.
import os# - Provides interfaces to interact with the operating system
from random import randint# - Imports function for generating random integers.
from datetime import datetime as dt# - Simplifies date and time manipulations using 'dt' alias.
from datetime import timedelta# - Enables arithmetic on dates and times 
import math as mt# - Access mathematical functions via 'mt' shortcut.

cwd =  os.getcwd()# - retrieves the current working directory (where the script is running).
print(cwd)
files = os.listdir()# - lists all the files and directories in the current directory specified by os.getcwd().
print(files)# - If no argument is given to os.listdir(), it defaults to the current directory.

for i in range(10):# - outputs a number ten times, integers 0 to 9.
    print(randint(1,100))# - Prints random number between 1 and 10.

    time = dt(2022, 6, 1,2,3,4)# - Creates a datetime object for June 1, 2022, at 02:03:04
    print(time)
    print(time+timedelta(2))# - Adds two days to the datetime object

print(mt.cos(3.14))# - Prints cosine of 3.14 using 'mt' command
