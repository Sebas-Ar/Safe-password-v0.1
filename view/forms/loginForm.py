import os
from getpass import getpass
from utils.loading import loading

def loginForm():
    '''
    form to user login, it verify fields are not empty,
    hide password and return those values
    '''
    print('\nLOGIN\n')
    userName = input('Enter your Username: ')
    password = getpass('Enter your Password: ')
    
    # Verify if fields are not empty
    if userName and password:
        loading('Verify login')
        return userName, password
    else:
        loading('Incomplete Data!')
        return loginForm()

