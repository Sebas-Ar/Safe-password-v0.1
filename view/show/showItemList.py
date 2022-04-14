import os

def showItemList(itemUserList):
    '''
    This interface show item list from a specific user
    '''

    os.system('clear')   
    print('\nITEM LIST')

    # Go through user's item list
    for itemUser in itemUserList:
        print(f'\nid: {itemUser["_id"]}')
        print(f'title: {itemUser["title"]}')
        print(f'URL: {itemUser["URL"]}')
        print(f'comment: {itemUser["comment"]}')

