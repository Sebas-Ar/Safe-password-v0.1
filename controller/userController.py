from utils.data import * 
from utils.encryp import *
from utils.generateId import *

def signupUser(userName, password, name):
    '''
    it create a new user, verify if already username exist
    '''
    
    # load data from data.json in model folder
    data = openData()
    # get item list from data
    userList = data["userList"]

    # To verify exist username
    userExist = False
    
    # Go through all user list
    for user in userList:
        # find equal user name inserted
        if user["userName"] == userName:
            # verify existing username
            userExist = True

    if not userExist:

        # Generate unique new id
        _id = generateId(userList)

        # Add user to user list
        userList.append({
            "_id": _id,
            "userName": userName,
            "password": encryptPass(password),
            "name": name
        })

        # Save data modified with the new user in user list
        saveData(data)

    return userExist

def signinUser(userName, password):
    '''
    it validate te user login and if he insert a valid 
    credential thrut, it return his id
    '''
    # load data from data.json in model folder
    data = openData()
    # get item list from data
    userList = data["userList"]

    # Go through all users from user list
    for user in userList:
        # verify username and password
        if user["userName"] == userName and decryptPass(user["password"]) == password:
            return True, user["_id"]

    return False, -1

def getUserData(_id):
    '''
    Get user data from a specific id and return his tag list and data user
    '''

    # load data from data.json in model folder
    data = openData()
    
    # get user list from data
    userList = data["userList"]
    # get tag list from data
    tagList = data["tagList"]

    # List where will save user tag list
    userTagList = []

    # Go through all tag list
    for tag in tagList:
        # Find tag from a specific user id
        if tag["userId"] == _id:
            # add tag to userTagList
            userTagList.append(tag["tag"])
    
    # Dictionary where will save user data
    userData = {}

    # Go through all user list
    for user in userList:
        # Find a specific user by a user id
        if user["_id"] == _id:
            # add user information to userData
            userData["info"] = user
            break

    # add tag list to user list
    userData["tags"] = userTagList

    return userData
        
