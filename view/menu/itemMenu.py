import os
from utils.loading import loading

ADD_ITEM = 1
SEE_ITEM_LIST = 2
GO_BACK = 3

def itemMenu():
    '''
    Menu item where user is able to choose an option between add item,
    see an item or go back to main menu
    '''
    os.system('clear')

    print('\nITEM MENU')

    print('\n1 -> Add Item')
    print('2 -> See Item list')
    print('3 -> Go Back main menu')
    
    try:
        option = int(input('\nChoose a number: '))
    except:
        loading('Is not number!')
        # to see this menu again
        return itemMenu()
    else:
        if option >= ADD_ITEM and option <= GO_BACK:
            os.system('clear')
            # to see selected option
            return option
        else:
            loading('Number out range!')
            # to see this menu again
            return itemMenu()
