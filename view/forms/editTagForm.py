import os
from utils.loading import loading

def editTagForm(tagName, tagList):
    '''
    form to edit tag, it receive a tag name and user tag list to verify
    if tag already exist or field is empety
    '''
    os.system('clear')

    print('\nEDITING TAG')
    print('\nEnter new input for edit the tag, for no edit, let input empty')
    print('Text between brackets is current tag')

    # show current tag name in the input
    updatedTag = input(f'\nTag ({tagName}): ')

    # Go through all user tag lisit
    for tag in tagList:
        # vefiry if tag already exist
        if tag == updatedTag:
            loading('tag name already exist')
            return editTagForm(tagName, tagList)
    if not updatedTag:
        loading('empty input!')
        return editTagForm(tagName)

    return updatedTag
