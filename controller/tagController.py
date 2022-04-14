from utils.data import *
from utils.generateId import *

def addTag(userId, tag):
    '''
    it create a new tag with a unique id, it linked to a specify user
    '''
    # load data from data.json in model folder
    data = openData()
    # get item list from data
    tagList = data["tagList"]

    _id = generateId(tagList)
    # add tag to tag list
    tagList.append({
        "_id": _id,
        "userId": userId, 
        "tag": tag
    })
    # save data modified with new tag added
    saveData(data)

def getTagList(_id):
    '''
    it get all tags in tag list from a specify user by his id
    '''
    # load data from data.json in model folder
    data = openData()
    # get tag list from data
    tagList = data["tagList"]
    # List where will save tag by a specify user
    userTagList = []
    # Go where all tag list
    for tag in tagList:
        # foun tag with id specify
        if tag["userId"] == _id:
            # Save the tag in userTagList
            userTagList.append(tag)

    return userTagList

def getItemOfTag(userId, tagName):
    '''
    get item list where each contain a specify tag added in it
    '''
    # load data from data.json in model folder
    data = openData()
    # get item list from data
    itemList = data["itemList"]
    # List where will save items by a specify tag
    itemOfTag = []
    # Go through all item list
    for item in itemList:
        # find item by a specific user
        if item["userId"] == userId:
            # Go through all linked tags to item
            for tag in item["tagList"]:
                # Find tag specify in item's tags
                if tag == tagName:
                    # save item in itemOfTag
                    itemOfTag.append(item)
                    break

    return itemOfTag

def deleteTag(itemListOfTag, tagUser):
    '''
    delete an tag from tag list and in each item that contain it in his own tag list
    '''

    # load data from data.json in model folder
    data = openData()
    # get item list from data
    itemList = data["itemList"]
    # get tag list from data
    tagList = data["tagList"]

    # Go through all item list
    for item in itemList:
        # Go through all item List from a specific tag
        for itemOfTag in itemListOfTag:
            # find tag in item's tags
            if item == itemOfTag:
                # delete tag in item's tags
                item["tagList"].remove(tagUser["tag"])
                break
    
    # delete tag from tag list
    tagList.remove(tagUser)

    # save data modified without the tag deleted in tag list and in items tags
    saveData(data)


def updateTag(userId, tagUser, newTag):
    '''
    update an tag from tag list and in each item that conaint it in its own tag list
    '''
    """ input(f'{userId}')
    input(f'{tagUser}')
    input(f'{newTag}') """
    # load data from data.json in model folder
    data = openData()
    # get item list from data
    itemList = data["itemList"]
    # get tag list from data
    tagList = data["tagList"]

    # To verify if already exist the tag modified in user tags list
    alreadyTagExist = False
    # Go through all item list
    for tag in tagList:
            if tag["userId"] == userId:
                """ input(f'{tag}')
                input(f'{tagUser}') """
                if tag['tag'] == newTag:
                    alreadyTagExist = True

    if not alreadyTagExist:
        """ input(f'enter here') """
        # Go through all item list
        for item in itemList:
            # Fin items by a specific user
            if item["userId"] == userId:
                # Go through all tag in items tags
                for tag in item["tagList"]:
                    # find the specific tag to update
                    if tag == tagUser["tag"]:
                        # Remove old tag
                        item["tagList"].remove(tag)
                        # add new tag
                        item["tagList"].append(newTag)

        # Go through all tag list
        for tag in tagList:
            # Find tags by a specific user
            if tag["userId"] == userId:
                # Find the specific tag to update
                if tag == tagUser:
                    # replace new tag value
                    tag["tag"] = newTag

        # Replace tag to new value for the interface
        tagUser["tag"] = newTag

        # Save the data modified with the tag list and items tags updated
        saveData(data)


