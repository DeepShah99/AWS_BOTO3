import mysql.connector as mc

try: 
    mydb = mc.connect(
        host = 'rdsdemoudemy.cmeexn4btaah.us-east-1.rds.amazonaws.com',
        user = 'admin',
        password = 'rdsdemoudemy',
        database = 'udemyDB'
    )

    

    cursor = mydb.cursor()
    cursor.execute('INSERT INTO Person(FirstName, LastName) VALUES (%s, %s)', ("Deep", "Shah"))
    mydb.commit()
    
except mc.Error as e:
    print('failed to insert data {}'.format(e))
    
