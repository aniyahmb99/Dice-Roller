import random
import os

def numOfDie():
    while True:
        try:
            numDice = input('How many dice would you like to play with? ')
            valid_response = ['one', '1', '2', 'two']
            
            if numDice not in valid_response:
                raise ValueError('Please choose to play with either 1 or 2 die.')
            else:
                print(numDice + ' dice')
                return numDice
        except ValueError as err:
            print(err)
            

def rollDice():
    
    min_value = 1
    max_value = 6
    roll_again = 'y'
    while roll_again.lower() == 'yes' or roll_again.lower() == 'y':
        # clear screen if using windows os
        os.system('cls' if os.name == 'nt' else 'clear') 
        amount = numOfDie()
        
        #to actually roll dice
        if amount == '1' or amount == 'one':
            print('Rolling dice....')
            dice1 = random.randint(min_value, max_value)
            print('Dice 1: ', dice1)
            
        elif amount == '2' or amount == 'two':
            print('Rolling dice....')
            dice1 = random.randint(min_value, max_value)
            dice2 = random.randint(min_value, max_value)
            
            print('Dice 1: ', dice1)
            print('Dice 2: ', dice2 )
            print('Total: ', dice1 + dice2)
        else:
            return 
            
        roll_again = input('Do you want to roll again? ')
            
if __name__ == '__main__':
    rollDice()
                
