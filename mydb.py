# Install Mysql on your computer
# https://dev.mysql.com/downloads/installer/
# pip install mysql
# pip install mysql-connector-python
# pip install mysql-connector

import mysql.connector

"""con = mysql.connector.connect(host='localhost', password='root', user='root')

if con.is_connected():
    print('All done!')"""
dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'root'
)

#prepare a cursor object
cursorObject = dataBase.cursor()

#create a database
#cursorObject.execute("CREATE DATABASE mydata")

print("All done !")