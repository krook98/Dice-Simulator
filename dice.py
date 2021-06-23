import random

numbers = [1,2,3,4,5,6]

#Loop will repeat the block where it asks for input until 'n' is pressed.
while True:
    x = input("Would you like to roll the dice? Press 'y' for yes or 'n' for no.")
    if x == 'y':
        #Start rolling
        roll = random.randrange(numbers[0], numbers[5], 1)
        print(roll)
    elif x == 'n':
        #Say goodbye and exit
        print("Goodbye.")
        break



