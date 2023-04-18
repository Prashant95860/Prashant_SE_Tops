import tkinter 

screen = tkinter.Tk() # screen define

screen.title("My First Application") # use for set the title 
screen.geometry("500x500") # use for  screen size

# python function
def myfun():
    print("This is my python Function")

#display specific widget
#lbl = tkinter.Label(screen,text="Hello welcome to tkinter",font=("Arial",26,"bold"))
#lbl.pack()   if you want top and center use pack method

#lbl.place(x = 20,y= 50) # place method use for manuaaly place something in application

#btn1 = tkinter.Button(screen,text="Click Here",bg="black",fg="white",font=("Arial",26,"bold"),command=myfun)
# command use for execute function
#btn.place(x=20,y=120)

# greed method
btn1 = tkinter.Button(screen,text="Call 1",font=("Arial",28,"bold"))
btn1.grid(row=0,column=0)

btn2 = tkinter.Button(screen,text="Call 2",font=("Arial",28,"bold"))
btn2.grid(row=0,column=1)



# to execute screen
screen.mainloop()


