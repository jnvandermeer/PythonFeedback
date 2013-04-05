def saveobject(obj, filename):
    with open(filename, 'wb') as output:
        pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)

def loadobject(filename):
    with open(filename) as infileobj:
        obj=pickle.load(infileobj)
    return obj
        
