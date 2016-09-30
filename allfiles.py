import os

class AllFiles:
    def __init__(self, varList):
        self.target = varList['target']
    
    def getAllFiles(self):        
        return os.listdir(self.target) # take test form conf
