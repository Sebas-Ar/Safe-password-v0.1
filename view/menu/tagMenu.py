import os

ADD_TAG = 1
SEE_TAG_LIST = 2
GO_BACK = 3

def tagMenu():
    '''
    Tag menu where user is able to choose an option between add tag,
    see a tag or go back to main menu
    '''
    os.system('clear')

    print('\nTAG MENU')

    print('\n1 -> Add tag')
    print('2 -> See tag list')
    print('3 -> Go Back main menu')
    
    try:
        option = int(input('\nChoose a number: '))
    except:
        os.system('clear')
        print('\nNot a number!\n')
        # to see this menu again
        return tagMenu()
    else:
        if option >= ADD_TAG or option <= GO_BACK:
            os.system('clear')
            # to see selected option
            return option
        else:
            os.system('clear')
            print('\nNumber out range!\n')
            # to see this menu again
            return tagMenu()
