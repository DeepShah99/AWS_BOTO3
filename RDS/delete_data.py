import mysql.connector as mc

try: 
    mydb = mc.connect(
        host = 'rdsdemoudemy.cmeexn4btaah.us-east-1.rds.amazonaws.com',
        user = 'admin',
        password = 'rdsdemoudemy',
        database = 'udemyDB'
    )

    

    cursor = mydb.cursor()
    cursor.execute("DELETE FROM Person WHERE id = %s", ['2'])
    mydb.commit()
    print('data deleted')
    
except mc.Error as e:
    print('failed to delete data {}'.format(e))
    
