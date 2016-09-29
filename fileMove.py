import os
import shutil

target = "D:/WorkBench/Python/CleanJunk/test/"
destin = "D:/WorkBench/Python/CleanJunk/destin/"
filename = "Koala.jpg"

#shutil.copy("D:\WorkBench\Python\CleanJunk\destin\Koala.jpg", "test/Koala.jpg")
#shutil.copy("D:/WorkBench/Python/CleanJunk/destin/Koala.jpg", "test/Koala.jpg")
#shutil.move("test/Koala.jpg", "destin/Koala_copy.jpg")
#os.rename("test/Koala.jpg", "destin/Koala_copy.jpg")

#print os.path.abspath("destin")
#print os.path.isfile("D:/WorkBench/Python/CleanJunk/test/Koala.jpg")
targetName = filename

while (os.path.isfile(destin + targetName)):
    arr = targetName.strip().split('.')
    targetName = arr[0].strip() + '_copy.' + arr[1].strip()

if (os.path.isfile(target + filename)):
    shutil.move(target + filename, destin + targetName)
    #shutil.copy(target + filename, destin + targetName)
#os.rename(target + filename, destin + targetName)