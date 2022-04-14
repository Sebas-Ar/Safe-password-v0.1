

def deleteItemForm(itemUser):
    '''
    Form to delete item, receive an item and compare its id with id inserted
    by user for verify deleting  
    '''
    # item menu options
    DELETE_ITEM = 2 
    GO_ITEM_LIST = 4

    try:
        _id = int(input('\nfor permanently delete this item, enter its Id (Other number fo cancel deleting procces): '))
    except:
        print('\nNot a valid id, it must be a number!')
        return deleteItemForm(itemUser)
    else:
        # Verify if item is equal to id user inserted 
        if _id == itemUser["_id"]:
            # to delete and exit to item menu
            return GO_ITEM_LIST 

        # to repeat the deletion process
        return DELETE_ITEM
