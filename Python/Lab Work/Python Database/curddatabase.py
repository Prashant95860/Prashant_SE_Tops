#import pymysql
import pymysql

# connect with server

mydb = pymysql.connect(host="localhost",user="root",password="")
mycursor = mydb.cursor()

# create database
mycursor.execute("create database if not exists prashantbook")
mydb.commit()

# connect with database
mydb = pymysql.connect(host="localhost",user="root",password="",database="prashantbook")
mycursor = mydb.cursor()

# table creation
mycursor.execute("create table if not exists book12(id int primary key auto_increment, BookName varchar(20), Bookauthor varchar(20), Bookprice int, Bookpages int)")
mydb.commit()


