import mysql.connector
mydb=mysql.connector.connect(host='localhost', user='root',
                             password='1234', database='demo')
mycursor=mydb.cursor()
mycursor.execute("Select * from Emp")
result=mycursor.fetchall()
for i in result:
    print(i)