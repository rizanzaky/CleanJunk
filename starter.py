class ReadConf:
    __confFile = 'cleaner.conf'
    
    def getVarDictionary(self):
        f = open(self.__confFile, 'r')
        list = {}
        
        for line in f:
            line = line.strip()
            
            if (len(line) > 0 and line[0] != '#'):
                arr = line.split('=', 1)
                
                key = arr[0].strip()
                value = arr[1].strip()        
                
                if ((value[0] == '"' and value[-1] == '"') or (value[0] == "'" and value[-1] == "'")):
                    value = value[1 : len(value)-1]
                    
                list[key] = value
                
        f.close()
        return list
