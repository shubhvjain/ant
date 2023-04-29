import os
import util

def precheck():
    try:
        config = util.loadConfigFile()  
        keyFolderPathExists  = util.checkIfPathExists(config['keys']['path'])
        if(keyFolderPathExists):
            return True
        else:
            raise FileNotFoundError      
    except:
        print("Unable to fetch keys. Prechecks fail. Check the path to the keys folder in your configs")

def getKey(title):
    precheck()
    config = util.loadConfigFile() 
    keyFilePath = config['keys']['path']+ "/"+ util.formatString("single-nospace-dashsymbols",title)+".txt"
    absFilePath = util.getAbsolutePath(keyFilePath)
    keyFileExists = util.checkIfPathExists(keyFilePath)
    if keyFileExists:
        f = open(absFilePath,"r")
        firstLine = f.readline()
        return firstLine
    else:
        raise Exception("KeyNotFound") 

def setKey(title,value):
    precheck()
    config = util.loadConfigFile() 
    keyFilePath = config['keys']['path']+ "/"+ util.formatString("single-nospace-dashsymbols",title)+".txt"
    absFilePath = util.getAbsolutePath(keyFilePath)
    keyFileExists = util.checkIfPathExists(keyFilePath)
    if keyFileExists:
        raise Exception("keyAlreadyExists")
    else:
        f = open(absFilePath, "w")
        f.write(value)
        f.close()
        return "New file created : "+ keyFilePath