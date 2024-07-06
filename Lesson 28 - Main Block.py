def create_test_file():
    with open('test_file.py' , 'w') as file:# Open (or create) 'test_file.py' for writing
        file.write('''
def main():
    print(__file__)
    print(f'__name__ = {__name__}')

if __name__ == '__main__':
    main()
''')
#Make sure your indentation is incorrect 
def main():# Define the main function of the current script
    print(__file__)# Print the name of the current file
    print(f'__name__= {__name__}')# Print the __name__ attribute of the current script
    create_test_file()# Call the function to create 'test_file.py'
    import test_file # Import the newly created 'test_file' module
    test_file.main()# Call the main function from 'test_file'

if __name__ == '__main__':  # Check if the script is run directly
    main() # If yes, then call the main function. make sure your indentation is correct. 
#make sure you have 2 underscore not 3 '__' is correct '___' is not correct