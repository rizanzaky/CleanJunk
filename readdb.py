import pypyodbc

class Database:
    def __init__(self, varList):
        self.driver = varList['driver']
        self.server = varList['server']
        self.database = varList['database']
        self.uid = varList['uid']
        self.password = varList['password']
        self.schema = varList['schema']
        self.table = varList['table']
        self.column = varList['column']
    
    def getValidFiles(self):
        conString = 'Driver={%s};Server=%s;Database=%s;uid=%s;pwd=%s' % (self.driver, self.server, self.database, self.uid, self.password)
        
        con = pypyodbc.connect(conString)
        cursor = con.cursor()
        SQL = 'SELECT %s FROM %s.%s' % (self.column, self.schema, self.table)
        cursor.execute(SQL)
        
        rows = cursor.fetchall()
        
        list = []
        for row in rows:
            list.append(row[0])
        
        cursor.close()
        con.close()
        
        return list