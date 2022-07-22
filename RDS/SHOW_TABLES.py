import mysql.connector as mc

try: 
    mydb = mc.connect(
        host = 'rdsdemoudemy.cmeexn4btaah.us-east-1.rds.amazonaws.com',
        user = 'admin',
        password = 'rdsdemoudemy',
        database = 'udemyDB'
    )

    

    cursor = mydb.cursor()
    cursor.execute('SHOW TABLES')
    for table in cursor:
        print(table)

except mc.Error as e:
    print('failed to show table {}'.format(e))
