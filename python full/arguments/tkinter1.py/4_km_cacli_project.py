from tkinter import *

window=Tk()
window.title("my first tk inter")
window.minsize(450,200)

# updateds of label 
def update_to_km():
    text=int(input.get())*1.60934
    label2.configure(text=text)

# labels
label1=Label(text="Is equal too :")
label1.grid(row=2,column=0)


label2=Label(text=" 0 ")
label2.grid(row=2,column=1)

label3=Label(text="Miles")
label3.grid(row=0,column=2)

label4=Label(text="Kms")
label4.grid(row=2,column=2)


input=Entry(width=10)
input.grid(row=0,column=1)

bt1=Button(text="press",width=8,command=update_to_km)
bt1.grid(row=3,column=1)


window.mainloop()