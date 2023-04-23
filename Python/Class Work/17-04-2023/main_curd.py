# import connecting file

import curddatabase
import pymysql

# connect with databse

mydb = pymysql.connect(host="localhost",user="root",password="",database="10feb_db")
mycursor = mydb.cursor()

status = True

while status:
    data = """
    
                Menu

            1) Store Data
            2) View Data
            3) Update Data
            4) Search Data
            5) Delete Data
    
    """
    print(data)

    choice = int(input("Enter Your Choice : "))
    if choice==1:
        name = input("Enter Your Name : ")
        subject = input("Enter Subject : ")

        # query for store data
        query = "insert into student23 (name,subject) values ('%s','%s')"
        args = (name,subject)
        mycursor.execute(query % args)
        mydb.commit()

    elif choice==2:
        # to fetch all the data
        query = "select * from student23"
        # execute (query)
        mycursor.execute(query)

        # to fetch all the datafrom query
        data = mycursor.fetchall()
        print(data)

    elif choice==3:
        #update data
        id = int(input("Enter Id : "))
        name = input("Enter Name : ")
        subject = input("Enter Subject : ")

        #query for update
        query = "update student23 set name = '%s', subject = '%s' where id = %s"
        args = (name,subject,id)
        mycursor.execute(query%args)
        mydb.commit()
        print("Updated Successfully!!")


    elif choice==4:
        # search data
        id = int(input("Enter Id : "))

        #query
        query = "select * from student23 where id = %s"
        #args
        args = (id)

        mycursor.execute(query%args)

        # retrive all data in row variable
        row = mycursor.fetchone()

        #id = 0 name = 1 subject =2  row wise data

        displayname = row[1]
        displaysubject = row[2]

        print("name = ",displayname)
        print("subject = ",displaysubject)


    elif choice==5:
        id = int(input("Enter Id : "))

        # query
        query = "delete from student23 where id = %s"
        #args
        args = (id)

        mycursor.execute(query%args)

        mydb.commit()
        print("Deleted Successfully!!")



    loop_choice = input("Do you want to perform more operations press y for yes and n for no : ")
    if choice=="n":
        status = False
        
        