import os
import json 
import re

CONFIGPATH="~/digitalAssistAnt/config.json"

def getAbsolutePath(somePath):
    return os.path.expanduser(somePath)

def checkIfPathExists(path):
    absPath = getAbsolutePath(path)
    pathCheck = os.path.exists(absPath)
    return pathCheck

def loadConfigFile():
    pathToFile =  getAbsolutePath(CONFIGPATH)
    try:
        with open(pathToFile, 'r') as f:
            data = f.read()
            config = json.loads(data)
            return config
    except (FileNotFoundError): 
        print("Config file not found at path ",CONFIGPATH)
        raise FileNotFoundError
    
def formatString(format,input):
    if format == "single-nospace-dashsymbols":
        print()
        str = re.sub(r'[^a-zA-Z0-9 -]',r'',input)
        str = str.replace(" ","-")
        return str
    return input