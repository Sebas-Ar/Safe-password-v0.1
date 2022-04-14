import os
from utils.loading import loading

def addTagForm(tagList = []):

    '''
    Form to add a new tag to user list tag, it verify if tag already exist
    and return the new tag
    '''

    print('\nADD TAG')

    # Verify already tag exist
    repeatTag = True

    while repeatTag:

        # suppose tag is not exist
        repeatTag = False
        newTag = input('\nEnte new tag: ')
        
        # Go through all user tag list
        for tag in tagList:
            # verify already tag exist
            if tag == newTag:
                loading(f'Tag "{newTag}" already exist, please enter other')
                # for repeat cycle again
                repeatTag = True

    return newTag

