import os
from utils.loading import loading

def tagListMenu(tagUserList):

    print('\nOPTIONS')
    
    print('\n1 -> See a tag')
    print('2 -> go back tag menu')
    try:
        option = int(input('\nChoose a number: '))
    except:
        loading('Is not a number!')
        return {}, 1
    else:
        if option == 1:

            tagSelected = input('\nEnter tag name for see it: ')
            
            for tagUser in tagUserList:
                if tagUser["tag"] == tagSelected:
                    return tagUser, 1

            loading('The item\'s name does not exist!')
            return {}, 1

        elif option == 2:
            return {'test': True}, 3
        else:
            loading('Number out range!')
            return {}, 1

