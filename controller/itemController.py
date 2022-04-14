from utils.data import *
from utils.encryp import *
from utils.generateId import generateId
from copy import copy


def addItem(userId, title, userName, password, URL, comment, tagList):
    '''
    it create a new item with a unique id
    '''

    # load data from data.json in model folder
    data = openData()
    # get item list from data
    itemList = data["itemList"]
    
    _id = generateId(itemList)
    # add item to item list
    itemList.append({
        "_id": _id,
        "userId": userId,
        "title": title,
        "userName": userName,
        "password": encryptPass(password),
        "URL": URL,
        "comment": comment,
        "tagList": tagList 
    })
    # save data modified with the new item added in data.json in model folder
    saveData(data)


def getItemList(_id):
    '''
    it get all items in item list from a specify user by his id 
    '''

    # load data from data.json in model folder
    data = openData()
    # get item list from data
    itemList = data["itemList"]
    # List where will save items by a specify user
    userItemList = []
    # Go through all item list
    for item in itemList:
        # find item with id specificy
        if item["userId"] == _id:
            # Save the item in userItemList
            userItemList.append(item)

    return userItemList


def deleteItem(item):
    '''
    delete an item from the item list with a item specify
    '''

    # load data from data.json in model folder
    data = openData()
    # get item list from data
    itemList = data["itemList"]
    # found index item from item list
    index = 0
    for i in itemList:
        if i == item:
            break
        index = index + 1
    # delete the item
    itemList[index:index + 1] = []
    # save data with item list without the deleted item in data.json in model folder
    saveData(data)
    

def updateItem(updateItem, itemUser):
    '''
    update a specify item with the new data that is received in updateItem 
    and compares them with original item for replace or not his data
    '''
    # load data from data.json in model folder
    data = openData()
    # get item list from data
    itemList = data["itemList"]
    # encrypt the new password for the item to modified
    """ updateItem["password"] = encryptPass(updateItem["password"]) """
    # copy item dictionary
    validatedItem = copy(updateItem)

    # Validate each item value, if it contain text for replace content or else it is empty for to leave original content
    validatedItem["title"] = (itemUser["title"], validatedItem["title"])[validatedItem["title"] != ''] 
    validatedItem["userName"] = (itemUser["userName"], validatedItem["userName"])[validatedItem["userName"] != '']
    validatedItem["URL"] = (itemUser["URL"], validatedItem["URL"])[validatedItem["URL"] != ''] 
    validatedItem["comment"] = (itemUser["comment"], validatedItem["comment"])[validatedItem["comment"] != ''] 
    validatedItem["password"] = (itemUser["password"], encryptPass(validatedItem["password"]))[validatedItem["password"] != '']
    # get index from a specify item
    indexItem = itemList.index(itemUser)
    # replace actually item with the new item
    itemList[indexItem] = validatedItem
    # save data with the item updated in item list
    saveData(data)

    return validatedItem

