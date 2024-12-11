from tkinter import *

window=Tk()
window.title("my first tk inter")
window.minsize(500,300)

def button_clicked():
    print("hoo yeah...........!")
    label1.config(text="Button clicked")
    
    
def button_clicked1():
    input1=input.get()
    label1.config(text=input1)
    # label1.pack()

# labels
label1=Label(text="New Button")
label1.grid(row=0,column=0)

# buttons
bt1=Button(text="press",command=button_clicked)
bt1.grid(row=1,column=1)
bt1=Button(text="press 2 ",command=button_clicked1)
bt1.grid(row=0,column=2)

# bt1.pack()input
input=Entry(width=10)
input.grid(row=2,column=3)

# # text boc 
# box=Text(width=10,height=2)
# box.focus()
# box.pack()


window.mainloop()
