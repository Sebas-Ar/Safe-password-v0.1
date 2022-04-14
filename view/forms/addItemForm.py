import os
from utils.loading import loading

def addItemForm(allTags = []):
    '''
    Form to add a new item, it receive a user tag list and return item data
    '''

    # Clean screen
    os.system('clear')

    print('\nADD ITEM')

    title = input('\nEnter title: ')
    username = input('\nEnter username: ')
    password = input('\nEnter password: ')
    URL = input('\nEnter URL: ')
    comment = input('\nEnter comment: ')

    # verify all fields are not empty
    if title and password and URL and comment and username:

        # List where will save item's tags
        tagListUser = []

        # Verify if user has created tags
        if len(allTags) != 0:

            print('\nChoose tags to link')
            print('\nTag list:')

            # Number to select a tag
            tagNum = 1

            # Go through user tag list to show each one which respective option number
            for tag in allTags:
                print(f'{tagNum} -> {tag}')
                tagNum = tagNum + 1

            print(f'{tagNum} -> Finish tag selection and create item')
            
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
                        tagSelected = allTags[select - 1]

                        # Verify tag is not in item tag list
                        if not tagListUser.count(tagSelected):
                            # add tag to item tag list
                            tagListUser.append(tagSelected)
                            print(f'\nTag "{tagSelected}" added')
                            
                        # verify tag is in item tag list
                        else:
                            # remove tag to item tag list
                            tagListUser.remove(tagSelected)
                            print(f'\nTag "{tagSelected}" removed')

                        print('\nCurrent tag list:')
                        # Show current item tag list
                        for tag in tagListUser:
                            print(f'- {tag}')
                    # Verify the option to finish the tag selection
                    elif select == tagNum:
                        print('test')
                        break
                    else:
                        select = 1
                        print('\nNumber out range!')
        else:
            loading('Creating Item \n\t\tTo add tags, you have to create it first in tags menu, then edit this item', timeInterval=.4)

        return title, username, password, URL, comment, tagListUser

    else:
        loading('you can\'t let inputs empty!')
        return addItemForm()

    
