import os

EDIT_TAG = 1
DELETE_TAG = 2
EXIT_TAG = 3

def showTag(itemOfTag, tagName):

    '''
    Show item list from a specifi tag from an user
    '''

    os.system('clear')
    print(f'\nITEM LIST OF TAG: {tagName}')

    if len(itemOfTag):
        for item in itemOfTag:
            print(f'\n\tId: {item["_id"]}')
            print(f'\tTitle: {item["title"]}')
            print(f'\tUsername: {item["userName"]}')
            print(f'\tURL: {item["URL"]}')
    else:
        print('\nThere no items linked, to link you have to edit an item.')

    print('\nOptions')
    print('\n1 -> Edit tag')
    print('2 -> Delete tag')
    print('3 -> Go back to tag list')

    try:
        option = int(input('\nChoose a number: '))
    except:
        os.system('clear')
        print('\nNot a number\n')
        # to see this inteface again
        return showTag(itemOfTag, tagName)
    else:
        if option == EDIT_TAG:
            os.system('clear')
            # to see selected option
            return option
        elif option == EXIT_TAG:
            os.system('clear')
            # to see selected option
            return 4
        elif option == DELETE_TAG:
            # to see selected option
            return option
        else:
            os.system('clear')
            print('\nNumber out Range!\n')
            # to see this inteface again
            return showTag(itemOfTag, tagName)




