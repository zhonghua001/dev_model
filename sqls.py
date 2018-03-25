import pyodbc

print(pyodbc.drivers())

conn = pyodbc.connect(r'DRIVER={SQL Server Native Client 11.0};SERVER=192.168.0.200,1433;'
                      r'DATABASE=test;UID=hotel_user;PWD=123456;ApplicationIntent=ReadOnly')

cur = conn.cursor()

cur.execute('select @@servername;select * from sys.all_objects')

for i in cur:
    print(i)
cur.nextset()
a = [x[0] for x in cur.description]

for i in cur:
    print(dict(zip(a,i)))

