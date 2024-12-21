from tkinter import*

import requests as rq


def update_quote():
    quote=rq.get(url="https://api.kanye.rest")
    quote.raise_for_status()
    tupl=(quote.json()['quote'])
    canvas.itemconfig(quote_text,text=tupl)


window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="day33_bg.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote etha", width=250, font=(
    "Arial", 20, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="day33_kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0,command=update_quote)
kanye_button.grid(row=1, column=0)

window.mainloop()