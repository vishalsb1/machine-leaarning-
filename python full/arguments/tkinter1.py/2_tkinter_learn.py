from tkinter import *

window=Tk()
window.title("my first tk inter")
window.minsize(500,300)

def button_clicked():
    print("hoo yeah...........!")
    label1.config(text="Button clicked")
    # label1.pack()
    
def button_clicked1():
    input1=input.get()
    label1.config(text=input1)
    # label1.pack()

# labels
label1=Label(text="New Button")
label1.pack()

# buttons
bt1=Button(text="press",command=button_clicked1)

# bt1.pack()input
input=Entry(width=10)
input.pack()

# text boc 
box=Text(width=10,height=2)
box.focus()
box.pack()


window.mainloop()