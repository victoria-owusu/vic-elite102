import mysql.connector

 

connection = mysql.connector.connect(user = 'root', database ='bank', password = 'Katyisd#1')

cursor = connection.cursor()

testQuery = ("SELECT * FROM transactions")
cursor.execute(testQuery)

for item in cursor:
    print(item)

cursor.close()
connection.close()