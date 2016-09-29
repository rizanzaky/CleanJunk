import pyodbc

conString = 'Driver={SQL Server Native Client 11.0};Server=PROBOOK4540S\SQLEXPRESS;Database=CleanerDb;uid=sa;pwd=abc@123'
#cnxn = pyodbc.connect('DRIVER=CEMEXHRM\SQLEXPRESS;SERVER=localhost;DATABASE=CemexDb_Master_6;UID=cemex;PWD=abc@123')
cnxn = pyodbc.connect(conString)
#pyodbc.connect(r'DRIVER={SQL Server Native Client 11.0};SERVER=localhost;DATABASE=CemexDb_Master_6;UID=cemex;PWD=abc@123')
cursor = cnxn.cursor()
cursor.execute("SELECT * FROM dbo.CleanerTest")
rows = cursor.fetchall()
for row in rows:
    print row
    
cursor.close()
cnxn.close()