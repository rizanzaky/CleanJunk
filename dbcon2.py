import pypyodbc

conString = 'Driver={SQL Server Native Client 11.0};Server=PROBOOK4540S\SQLEXPRESS;Database=CleanerDb;uid=sa;pwd=abc@123'

con = pypyodbc.connect(conString)
cursor = con.cursor()
SQL = 'SELECT * FROM dbo.CleanerTest'
cursor.execute(SQL)

rows = cursor.fetchall()
for row in rows:
    print row

cursor.close()
con.close()