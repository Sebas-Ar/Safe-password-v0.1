import os
from getpass import getpass
from utils.loading import loading

def signupForm():
    '''
    signup Interface for new user, it verify fiels are not empty
    and equality between both inserted passwords
    '''

    print('\nSIGNUP\n')
    userName = input('Enter your Username: ')
    password = getpass('Enter your Password: ')
    repeatPassword = getpass('repeat Password: ')
    name = input('Enter your Name: ')

    # verify empty fields
    if userName and password and repeatPassword and name:
        # verify equal passwords
        if password == repeatPassword:
            # loading interface
            loading('Registering User')
            # clean screen
            os.system('clear')
            return userName, password, name
        else:
            # loading interface
            loading('passwords don\'t match')
            # clean screen
            os.system('clear')
            return signupForm()

    # loading interface
    loading('Incomplete Data')
    # clean screen
    os.system('clear')
    return signupForm()

