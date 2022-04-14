import time
from utils.loading import loading
from getpass import getpass

def editItemForm(itemUser, userTags, decryptPass):
    '''
    Form to edit item, it receive current item data, user tag list and password decrypted,
    then return the item data to update it
    '''
    print('\nEDITING ITEM')

    print('\nEnter new input for edit each attribute, for no edit, let input empty')
    print('Text between brackets is current value\n')

    # Show current item data in each input
    title = input(f'Title ({itemUser["title"]}): ')
    userName = input(f'Username ({itemUser["userName"]}): ')
    password = getpass(f'Password ({decryptPass}): ')
    URL = input(f'URL ({itemUser["URL"]}): ')
    comment = input(f'Comment ({itemUser["comment"]}): ')

    # Save updated input data
    updatedItem = {
        "_id": itemUser["_id"],
        "userId": itemUser["userId"],
        "title": title,
        "userName": userName,
        "password": password,
        "URL": URL,
        "comment": comment,
    }

    # Verify if user has created tags
    if len(userTags) != 0:
        print('Current tag list:\n')

        # list where will save current item's tags
        tagList = []

        # Go through current item tag list to show each one
        if (len(itemUser["tagList"]) != 0):
            for tagItem in itemUser["tagList"]:
                tagList.append(tagItem)
                print(f'- {tagItem}')
        else:
            print('\tThere no link tags yet')

        print('\nSaved tag list to Choose:\n')

        # Number to select a tag
        tagNum = 1

        # Go through user tag list to show each one which respective option number
        for tag in userTags:
            print(f'{tagNum} -> {tag}')
            tagNum = tagNum + 1

        print(f'{tagNum} -> Finish tag selection and update item')

        # Option inserted by user
        select = 1

        # Verify the option selected is between option range valid 
        while select >= 1 and select <= tagNum:

            try:
                select = int(input('\nChoose a number to add tag, if tag already has added it wil removed: '))
            except:
                print('\nNot a number!')
                select = 1
            else:
                # Verify the option selected to do refernce to a tag
                if select >= 1 and select <= tagNum - 1:

                    # Tag selected by user
                    tagSelected = userTags[select - 1]

                    # Verify tag is not in item tag list
                    if not tagList.count(tagSelected):
                        # add tag to item tag list
                        tagList.append(tagSelected)
                        print(f'\nTag "{tagSelected}" added')
                    
                    # verify tag is in item tag lis
                    else:
                        # remove tag to item tag list
                        tagList.remove(tagSelected)
                        print(f'\nTag "{tagSelected}" removed')
                        
                    print('\nCurrent tag list:')
                    # Show current item tag list
                    for tag in tagList:
                        print(f'- {tag}')

                # Verify the option to finish the tag selection
                elif select == tagNum:
                    break
                else:
                    select = 1
                    print('\nNumber out range!')

        updatedItem["tagList"] = tagList

    else:
        updatedItem["tagList"] = []
        loading('There no Tags in your current tag List, please create tags in tag menu')

    return updatedItem

