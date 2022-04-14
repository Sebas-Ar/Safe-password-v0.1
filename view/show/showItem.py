import os
from utils.loading import loading

EDIT_ITEM = 1
DELETE_ITEM = 2 
EXIT_ITEM = 3

def showItem(item, password):
    '''
    This interface shows data from a specific item and show to user
    optios to edit or delete this item
    '''

    os.system('clear')
    print(f'\nITEM: {item["title"]}')

    print(f'\nId: {item["_id"]}')
    print(f'Title: {item["title"]}')
    print(f'username: {item["userName"]}')
    print(f'Password: {password}')
    print(f'URL: {item["URL"]}')
    print(f'Comment: {item["comment"]}')
    print(f'Tag List:')

    # Go through item's tag list and show them
    if len(item["tagList"]):
        for tag in item["tagList"]:
            print(f'\t- {tag}')
    else:
        print('\tThere no tags, edit item to add')

    print('\nOptions:')
    print('\n1 -> Edit Item')
    print('2 -> Delete Item')
    print('3 -> Go back to item list')

    try:
        option = int(input('\nChoose a number: '))
    except:
        loading('Not a number!')
        # to see this inteface again
        return showItem(item, password)
    else:
        if option == EDIT_ITEM or option == EXIT_ITEM:
            os.system('clear')
            # to see selected option
            return option
        elif option == DELETE_ITEM:
            # to see selected option
            return option
        else:
            # to see this inteface again
            loading('Number out range!')
            return showItem(item, password)
