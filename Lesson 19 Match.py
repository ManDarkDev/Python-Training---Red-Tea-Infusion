command = input('Choose a greeting: ')
match command:
    case '1':
            print('Hi')
    case '2':
            print('Hello')
    case _:
          # The line `print('Invalid choice')` is part of the code block that is executed when the
          # user input does not match any of the specified cases in the `match` statement. In this
          # case, if the user enters a value other than '1' or '2', the program will print 'Invalid
          # choice'.
          print('Invalid choice')
#For some reason the choose a greeting command is not working in this terminal

item = '-2'
match item:
    case int(x) if x > 0:
        print('item is a positive number' , x)
    case str(x):
        print('item is a string', x)
    case list(x):
        print('item is a list' , x)