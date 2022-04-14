import os
from utils.loading import loading

ITEM = 1
TAG = 2
CLOSE = 3

def mainMenu(name):

    '''
    user program's main menu, he is able to go to 
    item menu, tag menu, or leave to programm
    '''

    print(f'\nWelcome {name}')
    print('\nUSER MENU:')
    print('\n1 -> Items')
    print('2 -> Tags')
    print('3 -> Close session')

    try:
        option = int(input('\nChose a number: '))
    except:
        loading('Not a number!')
        # to see this menu again
        return mainMenu(name)
    else:
        if  option >= 1 and option <= 3:
            os.system('clear')
            # to see selected option
            return option
        else:
            loading('Number out range!')
            # to see this menu again
            return mainMenu(name)


