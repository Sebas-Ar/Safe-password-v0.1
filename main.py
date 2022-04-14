import os

from view.welcome import *

from controller.userController import *
from controller.itemController import *
from controller.tagController import *

from utils.encryp import *
from utils.loading import loading

from view.menu.mainMenu import *
from view.menu.itemMenu import *
from view.menu.tagMenu import *
from view.menu.itemListMenu import *
from view.menu.tagListMenu import tagListMenu

from view.forms.addItemForm import addItemForm
from view.forms.addTagForm import addTagForm
from view.forms.deleteItemForm import deleteItemForm
from view.forms.deleteTagForm import deleteTagForm
from view.forms.signupForm import signupForm
from view.forms.loginForm import loginForm
from view.forms.editTagForm import editTagForm
from view.forms.editItemForm import editItemForm

from view.show.showItemList import *
from view.show.showTagList import showTagList
from view.show.showItem import *
from view.show.showTag import *


def main():
    '''
    Main funtio to turn on the program
    '''

    while True:
        # clean screen
        os.system('clear')
        # initialize the login in false
        isLogged = False
        # initialize an id not valid
        _id = -1

        while not isLogged:
            # Show welcome interfaz and return option to login or register
            isAccountExist = welcome()

            if isAccountExist == YES:
                # show login form and return username and password
                userName, password = loginForm()

                # validate username and password in data.js and return a valid login and the user id
                isLogged, _id = signinUser(userName, password)
                if not isLogged:
                    loading('Incorrect username or password')

            elif isAccountExist == NO:
                # show register form and return username, password and name
                userName, password, name = signupForm()

                # Register user data in data.js and return if already user exist
                userExist = signupUser(userName, password, name)
                if userExist:
                    loading('User already registered')

        # get data from the an id specific
        userData = getUserData(_id)
        # initialize the option to control the main menu
        mainMenuOpt = 1
        # initialize the option to control the item menu
        itemOpt = GO_BACK_ITEM_MENU

        while mainMenuOpt == ITEM or mainMenuOpt == TAG:
            # show main menu for delect item or tag option
            mainMenuOpt = mainMenu(userData["info"]["name"])

            if mainMenuOpt == ITEM:
                # initialize the optio to contro the item menu
                itemMenuOpt = ADD_ITEM

                while itemMenuOpt == ADD_ITEM or itemMenuOpt == SEE_ITEM_LIST:

                    if itemOpt == GO_BACK_ITEM_MENU:
                        # show item menu to select to add, see, or go back options.
                        itemMenuOpt = itemMenu()

                    if itemMenuOpt == ADD_ITEM:

                        # Show form to add an item and get the item parameters
                        title, username, password, URL, comment, tagList = addItemForm(userData["tags"])
                        # save item in data.josn 
                        addItem(_id, title, username, password, URL, comment, tagList)

                    elif itemMenuOpt == SEE_ITEM_LIST:

                        # intialize the item selecte
                        itemSelected = {}
                        while not itemSelected:

                            # get item list from a user id
                            itemUserList = getItemList(_id)
                            # Show the item list
                            showItemList(itemUserList)
                            # show menu to selec an option between delete, edit or go back option
                            itemSelected, itemOpt = itemListMenu(itemUserList)

                        while itemOpt == EDIT_ITEM or itemOpt == DELETE_ITEM:

                            # Decrypt the password
                            decryptPassword = decryptPass(itemSelected["password"])

                            # Show data from a specify item
                            itemOpt = showItem(itemSelected, decryptPassword)

                            if itemOpt == EDIT_ITEM:
                                # Show form to insert new data for the item specify
                                updatedItem = editItemForm(itemSelected, userData["tags"], decryptPassword)
                                # Save new ite in data.js
                                validatedItem = updateItem(updatedItem, itemSelected)
                                # Save the new item for show in interfaze
                                itemSelected = validatedItem
                            elif itemOpt == DELETE_ITEM:
                                # show form to select if delete or not an item.
                                itemOpt = deleteItemForm(itemSelected)
                                if itemOpt == 4:
                                    # delete the item from the data.json
                                    deleteItem(itemSelected)

            elif mainMenuOpt == TAG:

                # initialize the tag menu option
                tagMenuOpt = ADD_TAG
                # initialize the tag item menu option
                tagOpt = 3

                while tagMenuOpt == ADD_TAG or tagMenuOpt == SEE_TAG_LIST:
                    if tagOpt == 3:
                        # Show tag menu with option to add and see and item and go back
                        tagMenuOpt = tagMenu()

                    if tagMenuOpt == ADD_TAG:
                        # show form to inser new tag
                        tag = addTagForm(userData["tags"])
                        # save new tagg
                        addTag(_id, tag)
                        # add tag to interface
                        userData["tags"].append(tag)

                    elif tagMenuOpt == SEE_TAG_LIST:
                        # get tag list form a specific user
                        tagUserList = getTagList(_id)
                        # show tag list
                        showTagList(tagUserList)
                        # show menu for tag list, to see or go back
                        tagUser, tagOpt = tagListMenu(tagUserList)

                        while tagOpt == EDIT_TAG or tagOpt == DELETE_TAG:
                            # get items from a specifi tag
                            itemOfTag = getItemOfTag(_id, tagUser["tag"])
                            # Show tag option to delete, edit and go back
                            tagOpt = showTag(itemOfTag, tagUser["tag"])

                            if tagOpt == EDIT_TAG:
                                # Show form to insert new data to edit tag
                                updatedTag = editTagForm(tagUser["tag"], userData["tags"])
                                # remove tag from interface
                                userData["tags"].remove(tagUser["tag"])
                                # save tag in data.json
                                updateTag(_id, tagUser, updatedTag)
                                # Update tad in interface
                                tagUser["tag"] = updatedTag
                                # add modified tag in user data
                                userData["tags"].append(updatedTag)

                            elif tagOpt == DELETE_TAG:
                                # Show form to delete an specific tag
                                tagOpt = deleteTagForm(tagUser)
                                if tagOpt == 4:
                                    # Delete tag from data.json
                                    deleteTag(itemOfTag, tagUser)
                                    # remove tag from the user Data
                                    userData["tags"].remove(tagUser["tag"])

        loading(f'Goobye {userData["info"]["name"]}')


main()
