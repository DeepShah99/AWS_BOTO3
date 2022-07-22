import mysql.connector as mc

try: 
    mydb = mc.connect(
        host = 'rdsdemoudemy.cmeexn4btaah.us-east-1.rds.amazonaws.com',
        user = 'admin',
        password = 'rdsdemoudemy',
        database = 'udemyDB'
    )

    

    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM Person")
    for data in cursor:
        print(data)
    
except mc.Error as e:
    print('failed to show data in table {}'.format(e))
    
