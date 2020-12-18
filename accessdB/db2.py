import mysql.connector
mydb=mysql.connector.connect(host='localhost', user='root',
                             password='1234', database='demo')
mycursor=mydb.cursor()
mycursor.execute("Select * from Emp")
for i in mycursor:
    print(i)