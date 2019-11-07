
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
x=None
def action():
    if x==None:
        messagebox.showinfo("Status","UnSuccessful!!")
    else:
        messagebox.showinfo("Status","successful!!")
def valid():
    global x
    x=str(var.get())
    
w=Tk()
w.title("Movie Ticket Booking")
w.geometry("400x650")
lbl1=Label(w,text="Language:")
lbl1.grid(row=0,column=0)
var=IntVar()
r1=Radiobutton(w,text="English",variable=var,value=1,command=valid)
r2=Radiobutton(w,text="Hindi",variable=var,value=2,command=valid)
r3=Radiobutton(w,text="Kannada",variable=var,value=3,command=valid)
r1.grid(row=1,column=1)
r2.grid(row=1,column=2)
r3.grid(row=1,column=3)
lbl2=Label(w,text="Movie:")
lbl2.grid(row=3,column=0)
c1=Checkbutton(w,text="ABC")
c2=Checkbutton(w,text="DBC")
c3=Checkbutton(w,text="ACA")
c1.grid(row=4,column=1)
c2.grid(row=4,column=2)
c3.grid(row=4,column=3)
lbl3=Label(w,text="Number Of Tickets:")
lbl3.grid(row=6,column=0)
variable = StringVar()
variable.set("0")
dd = OptionMenu(w, variable, "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10")
dd.grid(row=7,column=1)

btn1=Button(w,text="Book Movie",command=action)
btn1.grid(row=10,column=1)
w.mainloop()


