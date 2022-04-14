import os
from utils.loading import loading

GO_BACK_ITEM_MENU = 3

def itemListMenu(itemUserList):
    '''
    Menu to see an item or get back to before menu, it receive user item list
    and return an item and selected user option
    '''

    SEE_ITEM = 1
    GO_BACK = 2

    print('\nOPTIONS')
    
    print('\n1 -> See an item')
    print('2 -> go back item menu')

    try:
        option = int(input('\nChoose a number: '))
    except:
        loading('Is not a number!')
        # to see this menu again
        return {}, SEE_ITEM
    else:
        if option == SEE_ITEM:
            try:
                idSelected = int(input('\nEnter item Id for see it: '))
            except:
                loading('Is not a number!')
                # to see this menu again
                return {}, SEE_ITEM
            else:
                for itemUser in itemUserList:
                    if itemUser["_id"] == idSelected:
                        # to see a specific item
                        return itemUser, SEE_ITEM
                loading('The item\'s id does not exist!')
                # to see this menu again
                return {}, SEE_ITEM

        elif option == GO_BACK:
            return {'test': True}, GO_BACK_ITEM_MENU
        else:
            loading('Number out range!')
            # to see this menu again
            return {}, SEE_ITEM
