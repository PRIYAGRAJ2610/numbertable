from tkinter import *
def MulTable() :
    print("\n"*2)
    for x in range (1,11) :
        m = int(EnterTable.get())
        print("\t\t",(x),"x",(m),"=",(x*m),)
win = Tk()
win.geometry("200x200+600+150")
win.title("mutiplication table - by prs ")

EnterTable = StringVar()

total = StringVar()
dif = StringVar()
timetable = StringVar()

label = Label(win, text = "multiplication table by prs",font = 35,fg = "black",bg = "white")
label.grid(row = 1 , column = 6)


label = Label( win, text = "                                                    ")
label.grid(row = 2, column = 6)


entry1 = Entry(win,textvariable = EnterTable, justify = "center")
entry1.grid(row = 3 , column = 6)

label = Label(win,text =  "                                                     ")
label.grid(row = 4 , column = 6)


button1 = Button(win,text = "Number table",command = MulTable)
button1.grid(row=5,column = 6)

QUIT = Button(win,text = "quit",fg = "red",command = win.destroy)
QUIT.grid(row = 7 , column = 6 )
              
win.mainloop
