#The program is design for users to guess the outcome from rolling dice.....
import random
print('''
        Welcome to your five lucky rolling dice game
        Opportunity to become the next millionaire.
        You are allowed only five trials before you are asked to input another coin. BEST OF LUCK!!!
        If you get one of the die number correctly you get half a million
        But, if you get the two correctly BOOM! You are a millionaire
        ''')
for i in range (5):
    rollDice1 = random.randint(1,6)
    rollDice2 = random.randint(1,6)
    print('\t To roll the dice\n',
          '\t you need to insert a coin')
    a = eval(input('Enter random dice number between 1 to 6\n'))
    print('rolling dice....')
    if a == rollDice1:
        print('\t You sabi!!!, On your way to become a millionaire')
    else:
        print('\t OLODO!!!, Try to get even half')
    b = eval(input('Enter random dice number between 1 to 6\n'))
    print('rolling dice....')
    if b == rollDice2:
        print('\t SABI!!!')
    else:
        print('\t SORRY!!!')
    if a == rollDice1 and b == rollDice2:
        print('JACKPOT!!!')
    else:
        print('\t Sorry, input coin to try again\n',
              '\t the correct number is', rollDice1, 'and', rollDice2,',Try again')
