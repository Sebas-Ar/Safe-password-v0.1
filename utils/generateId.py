def generateId(list):
    '''
    generate a new id from last item's id from a list 
    '''
    _id = 0

    if len(list) != 0:
        # find id from last item and add one 
        _id = list[-1]["_id"] + 1

    return _id

