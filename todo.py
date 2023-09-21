from tkinter import *
from tkinter import messagebox
header=Tk()
header.title("To-Do list")
header.geometry("400x500+600+100")
header.resizable(False,False)
header.config(bg='#223441')

task=[]
a=[]
def addtask():
    task=my_task.get()
    if task!="":
        a.append(lb.insert(END,task))
        my_task.delete(0,"end")         # used to empty the entry box after inserting task
    else:
        messagebox.showwarning("warning","Task empty!!!")

def delete_task():
    lb.delete(ANCHOR)        # ANCHOR refers to a selected item over cursor.

frame= Frame(header)
frame.pack(pady=15)

lb = Listbox(
    frame,
    width=30,  
    height=8,
    font=('Arial',16),
    bd=0,
    fg='#464646',
    selectbackground='#a6a6a6',
    activestyle="none",
)

lb.pack(side=LEFT,fill=BOTH)

sb=Scrollbar(frame)
sb.pack(side=RIGHT,fill=BOTH)

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

my_task=Entry(
    header,
    font=('Arial',23),
    
    
    
)
my_task.pack(pady=30)
button_frame=Frame(header)
button_frame.pack(pady=20)

add_button=Button(
    button_frame,
    text="+",
    font="10",
    bg='#c5f776',
    fg='black',
    padx=35,
    pady=2,

    command=addtask
)
add_button.pack(fill=BOTH, expand=True, side=LEFT)

delete_button=Button(
    button_frame,
    text=('-'),
    font=('14'),
    bg='#ff8b61',
    padx=35,
    pady=10,
    command=delete_task
)
delete_button.pack(fill=BOTH, side=RIGHT)



header.mainloop()