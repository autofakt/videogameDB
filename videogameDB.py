import mysql.connector

cnx = mysql.connector.connect(user='root', password='blue5555',
                              host='127.0.0.1',
                              database='videogameDB')

mycursor = cnx.cursor()
'''
creates table
mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
'''

# Print all available tables
mycursor.execute("SHOW TABLES")

for x in mycursor:
    print(x)

from tkinter import Tk, Button, Label, Scrollbar, Listbox, StringVar, DoubleVar, IntVar, Entry, W, E, N, S, END
from tkinter import ttk
from tkinter import messagebox


class VideogameDB:
    def __init__(self):
        self.con = mysql.connector.connect(user='root', password='blue5555',
                                           host='127.0.0.1',
                                           database='videogameDB')
        self.cursor = self.con.cursor()
        print("You have connected to the database")
        print(self.con)
        print(self.cursor)

    # def __del__(self):
    #     self.con.close()

    def view(self):
        self.cursor.execute("SELECT * FROM games")
        rows = self.cursor.fetchall()
        return rows

    def insert(self,title,platform, price, quantity):
        sql = (f"INSERT INTO games (title,platform, price, quantity) VALUES ('{title}', '{platform}', {price}, {quantity});")
        print(sql)
        self.cursor.execute(sql)
        self.con.commit()
        messagebox.showinfo(title="Video Game Pro", message="New game added to database")

    def update(self, gid, title, platform, price, quantity):
        tsql = 'UPDATE games SET title = %s, platform = %s, price = %f, quantity = %d WHERE gid = %%d'
        self.cursor.execute(tsql, [title,platform,price,quantity,gid])
        self.con.commit()
        messagebox.showinfo(title="Game Datebase", message="Game updated")

    def __delete__(self, gid):
        delquery = 'DELETE FROM games WHERE gid = %d'
        self.cursor.execute(delquery, [id])
        self.con.commit()
        messagebox.showinfo(title="Game Datebase", message="Game Deleted")



def get_selected_row(event):
    global selected_tuple
    index = list_box.curselection()[0]
    selected_tuple = list_box.get(index)
    title_input.delete(0,'end')
    title_input.insert('end',selected_tuple[1])
    #Platform needs special case here
    price_input.delete(0,'end')
    price_input.insert('end',selected_tuple[3])
    q_input.delete(0,'end')
    q_input.insert('end',selected_tuple[4])

def view_records():
    list_box.delete(0,'end')
    for row in db.view():
        list_box.insert('end',row)

def add_game():
    db.insert(title_text.get(),platform_combo.get(), price_text.get(), q_text.get())
    list_box.delete(0,'end')
    list_box.insert('end',(title_text.get(),platform_combo.get(), price_text.get(), q_text.get()))
    title_input.delete(0,'end')
    platform_combo.set('')
    price_input.delete(0,'end')
    q_input.delete(0,'end')
    cnx.commit()

def delete_records():
    db.delete(selected_tuple[0])
    cnx.commit()

def clear_screen():
    list_box.delete(0,'end')
    title_input.delete(0,'end')
    platform_combo.set('')
    price_input.delete(0, 'end')
    q_input.delete(0, 'end')

def update_records():
    db.update(selected_tuple[0],title_text.get(), platform_combo.get(), price_text.get(), q_text.get())
    title_input.delete(0, 'end')
    platform_combo.set('')
    price_input.delete(0, 'end')
    q_input.delete(0, 'end')
    cnx.commit()

def on_closing():
    dd=db
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()
        del dd

db = VideogameDB()

root = Tk()

root.title("Video Game Pro")
root.configure(background="light blue")
root.geometry("1050x650")
root.resizable(width=False, height=False)

title_label = ttk.Label(root, text="Game Title: ", background="light blue", font=("TkDefaultFont", 16))
title_label.grid(row=0, column=0, sticky=W, pady=10, padx=3)

title_text = StringVar()
title_input = ttk.Entry(root, width=26, textvariable=title_text, font=("TkDefaultFont", 12))
title_input.grid(row=0, column=1, sticky=W)
title_input.focus()

platform_label = ttk.Label(root, text="Platform: ", background="light blue", font=("TkDefaultFont", 16))
platform_label.grid(row=0, column=2, padx=3)

platform_combo = ttk.Combobox(root, width=10, state="readonly", font=("TkDefaultFont", 12))
platform_combo.grid(row=0, column=3, sticky=W)
platform_combo['values'] = (' PS5',
                            ' PS4',
                            ' Xbox X',
                            ' Xbox One',
                            ' Switch',
                            ' PC'
                            )

price_label = ttk.Label(root, text="Price: ", background="light blue", font=("TkDefaultFont", 16))
price_label.grid(row=0, column=4, padx=3)

price_text = DoubleVar()
price_input = ttk.Entry(root, width=10, textvariable=price_text, font=("TkDefaultFont", 12))
price_input.grid(row=0, column=5, sticky=W)

q_label = ttk.Label(root, text="Quantity: ", background="light blue", font=("TkDefaultFont", 16))
q_label.grid(row=0, column=6, padx=3)

q_text = IntVar()
q_input = ttk.Entry(root, width=8, textvariable=q_text, font=("TkDefaultFont", 12))
q_input.grid(row=0, column=7, sticky=W)

add_btn = Button(root, text="Add Game", bg="blue", fg="white", font="helvetica 10 bold", command=add_game)
add_btn.grid(row=0, column=8, padx=30)

list_box = Listbox(root, height=16, font="helvetica 13", bg="light gray")
list_box.grid(row=3, column=0, columnspan=4, sticky=W + E)

scroll_bar = Scrollbar(root)
scroll_bar.grid(row=3, column=3)

list_box.configure(yscrollcommand=scroll_bar.set)
scroll_bar.configure(command=list_box.yview)

modify_btn = Button(root, text="Modify Record", bg="purple", fg="white", font="helvetica 10 bold", command="")
modify_btn.grid(row=4, column=2)

delete_btn = Button(root, text="Delete Record", bg="red", fg="white", font="helvetica 10 bold", command="")
delete_btn.grid(row=4, column=3)

load_btn = Button(root, text="Load Records", bg="cornflowerblue", fg="white", font="helvetica 10 bold", command="")
load_btn.grid(row=4, column=0)

clear_btn = Button(root, text="Clear Screen", bg="maroon", fg="white", font="helvetica 10 bold", command=clear_screen)
clear_btn.grid(row=4, column=1, sticky=W)

exit_btn = Button(root, text="Exit", bg="violetred", fg="white", font="helvetica 10 bold", command=on_closing)
exit_btn.grid(row=0, column=8, sticky=W)

root.mainloop()
