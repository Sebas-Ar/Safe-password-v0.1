import os
from utils.loading import loading

YES = 1
NO = 2

def welcome():
    '''
    This interface allow the user register and login in the program. 
    '''
    print('\nWelcome to Safe-Pass\n')
    print('Do you have an account?\n')
    print('1 -> Yes')
    print('2 -> No')

    try:
        response = int(input('\nChoose a number: '))
    except:
        loading('Not a number!')
    else:
        if response == YES or response == NO:
            os.system('clear')
            return response
        else:
            loading('Number out range!')
            return welcome()

