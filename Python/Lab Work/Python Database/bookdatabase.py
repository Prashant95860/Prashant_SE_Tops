import curddatabase
import pymysql

mydb = pymysql.connect(host="localhost",user="root",password="",database="prashantbook")
mycursor = mydb.cursor()

status = True

while status:
    data = """
    
                Menu

                1) Store Book Data
                2) View Book Data
                3) Update Book Data
                4) Search Book Data
                5) Delete Book Data
                6) Exit

    """
    print(data)

    choice = int(input("Enter Your Choice : "))
    if choice ==1:
        BookName = input("Enter Book Name : ")
        Bookauthor = input("Enter Book Author Name : ")
        Bookprice = int(input("Enter Book Price : "))
        Bookpages = int(input("Enter Book Pages : "))

        # query
        query = "insert into book12 (BookName,Bookauthor,Bookprice,Bookpages) values ('%s','%s',%s,%s)"
        args = (BookName,Bookauthor,Bookprice,Bookpages)
        mycursor.execute(query % args)
        mydb.commit()

        print("Data Succesfully Inserted")

    
    elif choice ==2:
        query = "select * from book12"
        mycursor.execute(query)

        data = mycursor.fetchall()
        print(data)

        
    elif choice ==3:
        # update data
        id = int(input("Enter Id : "))
        BookName = input("Enter Book Name : ")
        Bookauthor = input("Enter Book Author Name : ")
        Bookprice = int(input("Enter Book Price : "))
        Bookpages = int(input("Enter Book Pages : "))

        #query
        query = "update book12 set "

        




