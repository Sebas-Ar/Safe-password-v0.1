import json

def openData():
    '''
    open data.json and return its JSON data
    '''
    # open file
    fileOpen = open('model/data.json', 'r')
    # load data from file
    data = json.load(fileOpen)
    # close the file
    fileOpen.close()

    return data

def saveData(data):
    '''
    save JSON data in data.json
    '''

    # open file
    fileOpen = open('model/data.json', 'w')
    # insert JSON data in file with a formate JSON style
    json.dump(data, fileOpen, indent = 4, separators = (',', ': ') )
    # close the file
    fileOpen.close()
    

    
