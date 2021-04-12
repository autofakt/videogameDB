from tkinter import Tk,Button,Label,Scrollbar,Listbox,StringVar,DoubleVar,IntVar,Entry,W,E,N,S,END
from tkinter import ttk
from tkinter import messagebox

root = Tk()

root.title("Video Game Pro")
root.configure(background="light blue")
root.geometry("1050x650")
root.resizable(width=False,height=False)

title_label = ttk.Label(root, text="Game Title: ", background="light blue", font=("TkDefaultFont", 16))
title_label.grid(row=0, column=0,sticky=W, pady=10)

title_text = StringVar()
title_input = ttk.Entry(root,width=26, textvariable= title_text,font=("TkDefaultFont", 12))
title_input.grid(row=0, column=1, sticky=W)

platform_label = ttk.Label(root, text="Platform: ", background="light blue", font=("TkDefaultFont", 16))
platform_label.grid(row=0, column=2,sticky=W)

platform_combo = ttk.Combobox(root, width=10, state="readonly",font=("TkDefaultFont", 12))
platform_combo.grid(row=0, column=3, sticky=W)
platform_combo['values'] = (' PS5',
                          ' PS4',
                          ' Xbox X',
                          ' Xbox One',
                          ' Switch',
                          ' PC'
                          )

price_label = ttk.Label(root, text="Price: ", background="light blue", font=("TkDefaultFont", 16))
price_label.grid(row=0, column=4,sticky=W)

price_text = DoubleVar()
price_input = ttk.Entry(root,width=10, textvariable= price_text,font=("TkDefaultFont", 12))
price_input.grid(row=0, column=5, sticky=W)

q_label = ttk.Label(root, text="Quantity: ", background="light blue", font=("TkDefaultFont", 16))
q_label.grid(row=0, column=6,sticky=W)

q_text = IntVar()
q_input = ttk.Entry(root,width=8, textvariable= q_text ,font=("TkDefaultFont", 12))
q_input.grid(row=0, column=7, sticky=W)

add_btn = Button(root, text="Add Game", bg="blue", fg="white", font="helvetica 10 bold", command="")
add_btn.grid(row=0, column=8)

list_box= Listbox(root,height=16, width=40, font="helvetica 13", bg="light gray")
list_box.grid(row=3, column=1, columnspan=14, sticky=W +E, pady=0, padx=0)

scroll_bar = Scrollbar(root)
scroll_bar.grid(row=1, column=8, rowspan=14)

list_box.configure(yscrollcommand = scroll_bar.set)
scroll_bar.configure(command=list_box.yview)

root.mainloop()