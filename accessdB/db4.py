import mysql.connector
mydb=mysql.connector.connect(host='localhost', user='root',
                             password='1234', database='demo')
mycursor=mydb.cursor()
mycursor.execute("Select id,fname,lname,email from Emp")
result=mycursor.fetchone()
print(result)
#for i in result:
    #print(i)