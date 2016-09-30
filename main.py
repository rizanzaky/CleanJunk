from starter import ReadConf
from readdb import Database
from allfiles import AllFiles
from fileMove import MoveFiles

_varList = ReadConf().getVarDictionary()

validList = Database(_varList).getValidFiles()
validList.append('.hold')

allList = AllFiles(_varList).getAllFiles()

junkList = list(set(allList) - set(validList))

MoveFiles(_varList).moveFiles(junkList)
