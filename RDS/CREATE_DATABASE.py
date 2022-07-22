import mysql.connector as mc

try: 
    mydb = mc.connect(
        host = 'rdsdemoudemy.cmeexn4btaah.us-east-1.rds.amazonaws.com',
        user = 'admin',
        password = 'rdsdemoudemy'
    )

    dbname = input('please enter database name: ')

    cursor = mydb.cursor()
    cursor.execute('CREATE DATABASE ' + dbname)
    print('Database created')

except mc.Error as e:
    print('failed to create database')
