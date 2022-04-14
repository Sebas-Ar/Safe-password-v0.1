

def deleteTagForm(tagUser):
    '''
    Form to delete a tag, receive a tag and compare its name with an tag
    inserted by usert for verify the deletion
    '''

    # Tag menu options
    EDIT_TAG = 1
    EXIT_TAG = 4

    tagName = input('\nFor Permanetly delete this tag, enter its name, let input empty to cancel: ')

    # verify tag name inserted is equal to tag to delete
    if tagUser["tag"] == tagName:
        # to delete and exit to tag menu
        return EXIT_TAG
    elif tagName == '':
        # cancel deletion and exit to tag menu
        return EDIT_TAG
    else: 
        print('\nInput is not valid, please try again')
        return deleteTagForm(tagUser)
    
