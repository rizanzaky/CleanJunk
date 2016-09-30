import os
import shutil

class MoveFiles:
    #target = "D:/Rizan/LearningCurve/Python/CleanJunk/test/"
    #destin = "D:/Rizan/LearningCurve/Python/CleanJunk/destin/"
    def __init__(self, varList):
        self.target = varList['target']
        self.destin = varList['destin']
    
    def rectifiedTarget(self, _path):
        if (_path[-1] != '/'):
            _path += '/'
        elif (_path[-1] != '\\'):
            _path += '\\'
        
        return _path
        
    def moveFiles(self, files):
        #_target = self.rectifiedTarget(self.target)
        #_destin = self.rectifiedTarget(self.destin)
        
        _target = self.target
        _destin = self.destin
        
        for f in files:
            fileName = f.strip()
            targetName = fileName
            
            

            while (os.path.isfile(_destin + targetName)):
                arr = targetName.split('.')
                targetName = arr[0].strip() + '_copy.' + arr[1].strip()
            
            if (os.path.isfile(_target + fileName)):
                shutil.move(_target + fileName, _destin + targetName)
                
                print "Moved file %s successffully" % fileName
        
        return True
        
#shutil.copy(target + filename, destin + targetName)
#os.rename(target + filename, destin + targetName)
        
#shutil.copy("D:\WorkBench\Python\CleanJunk\destin\Koala.jpg", "test/Koala.jpg")
#shutil.copy("D:/WorkBench/Python/CleanJunk/destin/Koala.jpg", "test/Koala.jpg")
#shutil.move("test/Koala.jpg", "destin/Koala_copy.jpg")
#os.rename("test/Koala.jpg", "destin/Koala_copy.jpg")

#print os.path.abspath("destin")
#print os.path.isfile("D:/WorkBench/Python/CleanJunk/test/Koala.jpg")