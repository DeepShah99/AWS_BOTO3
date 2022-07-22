from tkinter import E
import mysql.connector as mc

try: 
    mydb = mc.connect(
        host = 'rdsdemoudemy.cmeexn4btaah.us-east-1.rds.amazonaws.com',
        user = 'admin',
        password = 'rdsdemoudemy'
    )

    print('connection successful')

except mc.Error as e:
    print('failed to connect {}'.format(e))
