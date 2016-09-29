import pyodbc

#cnxn = pyodbc.connect('DRIVER=CEMEXHRM\SQLEXPRESS;SERVER=localhost;DATABASE=CemexDb_Master_6;UID=cemex;PWD=abc@123')
cnxn = pyodbc.connect(r'DRIVER={SQL Server};SERVER=localhost;DATABASE=CemexDb_Master_6;Trusted_Connection=True;')
#pyodbc.connect(r'DRIVER={SQL Server Native Client 11.0};SERVER=localhost;DATABASE=CemexDb_Master_6;UID=cemex;PWD=abc@123')
cursor = cnxn.cursor()
cursor.execute("select * from HumanResource.Employee")
rows = cursor.fetchall()
for row in rows:
    print row.user_id, row.user_name