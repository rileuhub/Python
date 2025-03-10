"""This program will ask for the users name and favourite numbers
and then preforms math on the numbers"""

# Ask the user for their name and favourite numbers
name = input('What is your name? ')
number = int(input('What is your favourite number? '))
number2 = int(input('What is your second favourite number? '))

#preform some simple math on the numbers
add = number+number2
multiply = number*number2
minus = number-number2
#Greet the user and print the results
print(f'Hey {name}! Here are some calculations about your favourite numbers: ')
print(f'Your numbers added together = {add}')
print(f'Your numbers multiplied together = {multiply}')
print(f'Your numbers minused  = {minus}')
