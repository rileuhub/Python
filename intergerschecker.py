"""This program will check to see if the user has entered a valid number
in a specific range of values"""

# Use constants for the low and high values
LOW = 1
HIGH = 10

# Ask user to type in a number
num = input('Please enter an interger: ')

# Check to see if the number is valid
if num.lstrip("-").isnumeric():
    num = int(num)
    if num < LOW:
        print(f'{num} is lower than {LOW}')
    elif num > HIGH:
        print(f'{num} is greater than {HIGH}')
    else:
        print(f'Your number is {num}')
else:
    print(f'{num} is not an interger')
  