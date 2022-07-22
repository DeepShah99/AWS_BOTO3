import mysql.connector as mc

try: 
    mydb = mc.connect(
        host = 'rdsdemoudemy.cmeexn4btaah.us-east-1.rds.amazonaws.com',
        user = 'admin',
        password = 'rdsdemoudemy',
        database = 'udemyDB'
    )

    

    cursor = mydb.cursor()
    cursor.execute("UPDATE Person SET FirstName = %s WHERE id = %s", ('updated', '1'))
    mydb.commit()
    
except mc.Error as e:
    print('failed to update data {}'.format(e))
    
