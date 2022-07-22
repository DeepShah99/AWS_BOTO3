import mysql.connector as mc

try: 
    mydb = mc.connect(
        host = 'rdsdemoudemy.cmeexn4btaah.us-east-1.rds.amazonaws.com',
        user = 'admin',
        password = 'rdsdemoudemy',
        #database = 'udemyDB'
    )

    

    cursor = mydb.cursor()
    cursor.execute('USE udemyDB')
    cursor.execute('CREATE TABLE Person(id INT AUTO_INCREMENT PRIMARY KEY, FirstName VARCHAR(255), LastName VARCHAR(255))')
    print('Database created')

except mc.Error as e:
    print('failed to create table {}'.format(e))
