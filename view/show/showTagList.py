import os

def showTagList(tagUserList):
    '''
    This interfaz show tag list from a specific user
    '''
    os.system('clear')
    print('\nTAG LIST')

    if len(tagUserList):
        # Go through tag list from a specific user and show each one
        for tagUser in tagUserList:
            print(f'\n - {tagUser["tag"]}')
    else:
        print('\nThere no saved tags, you can add it in tag menu')

