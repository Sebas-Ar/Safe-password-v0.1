from cryptography.fernet import Fernet

def generateKey():
    '''
    generate new key for encrypt and decrypt passwords
    '''
    # generate the key from the cryptography library
    key = Fernet.generate_key()
    # save the key in a file clled secret.key
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

def loadKey():
    '''
    load the key from the secret.key file
    '''
    return open("secret.key", "rb").read()

def encryptPass(password):
    '''
    encryp a new password
    '''
    
    # load the key for encrypt
    key = loadKey()
    # use the key with cryptography library
    f = Fernet(key)
    # encode the string to utf-8 for to may encrypt it
    encodedPass = password.encode()
    # encryp the password
    encryptedPass = f.encrypt(encodedPass)
    # return the password encrypted decoded from utf-8
    return encryptedPass.decode('UTF-8')
    
def decryptPass(cryptedPass):
    '''
    decryp a new password
    '''
    # load the key for encrypt
    key = loadKey()
    # use the key with cryptography library
    f = Fernet(key)
    # encode the crypted password to utf-8 for to may decrypt it
    encodedPass = cryptedPass.encode('UTF-8')
    # decrypt the passowrd
    decryptedPass = f.decrypt(encodedPass)
    # return the password decrypted decoded from utf-8
    return decryptedPass.decode('UTF-8')
