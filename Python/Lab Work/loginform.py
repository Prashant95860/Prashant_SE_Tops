import random # import randmo for computer choice

import tkinter
screen = tkinter.Tk()
screen.geometry("400x400")

### logic implementation
l1 = ["Rock","Paper","Scissor"] # list for import random
def mygame(userchoice):
    print(userchoice)
    print("---->>display user choice")
    computerchoice = random.choice(l1)
    print(computerchoice)
    if userchoice==computerchoice:
        print("Match is Tie")
    


# display label
lbl = tkinter.Label(screen,text="Rock Paper Scissor",font=("Arial",22,"bold"))
lbl.pack()
# begin ---- rock,paper,scissor

e1 = tkinter.Button(screen,text="Rock",bg="blue",fg="white",font=("Arial",18,"bold"),command = lambda: mygame("Rock"))
# call the function
e1.place(x=50,y=80)

e2 = tkinter.Button(screen,text="Paper",bg="blue",fg="white",font=("Arial",18,"bold"),command = lambda: mygame("Paper"))
e2.place(x=150,y=80)

e3 = tkinter.Button(screen,text="Scissor",bg="blue",fg="white",font=("Arial",18,"bold"),command = lambda: mygame("Scissor"))
e3.place(x=250,y=80)

# end ---- rock,paper,scissor

#begin user code

e4 = tkinter.Label(screen,text="User",font=("Arial",14,"bold"))
e4.place(x=50,y=150)

e5 = tkinter.Label(screen,text="0",font=("Arial",14,"bold"))
e5.place(x=130,y=150)

e6 = tkinter.Label(screen,text="Computer",font=("Arial",14,"bold"))
e6.place(x=200,y=150)

e7 = tkinter.Label(screen,text="0",font=("Arial",14,"bold"))
e7.place(x=320,y=150)

# end : user scoreboard
e8 = tkinter.Label(screen,text="Result",bg="purple",fg="white",font=("Arial",24,"bold"),width=13,height=1)
e8.place(x=70,y=200)


screen.mainloop()