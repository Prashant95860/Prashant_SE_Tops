
# need to install xampp server or mysql
# after installation xampp server need to start apache server and mysql
# need to install pymysql --> pip install pymysql

# import pymysql
import pymysql

# connect with server (xampp or my sql)
mydb = pymysql.connect(host="localhost",user="root",password="")
mycursor = mydb.cursor()

# create data base
mycursor.execute("create database if not exists 10feb_db")
mydb.commit()

# connect with database
mydb = pymysql.connect(host="localhost",user="root",password="",database="10feb_db")
mycursor = mydb.cursor()

# table creation
mycursor.execute("create table if not exists student23(id int primary key auto_increment,name varchar(20),subject varchar(20))")
mydb.commit()   
