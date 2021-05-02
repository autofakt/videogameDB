from tkinter.ttk import Separator

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

from tkinter import Tk, Button, Label, Scrollbar, Listbox, StringVar, Frame, DoubleVar, IntVar, Entry, W, E, N, S, END
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk


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

    def viewBank(self, CID):
        self.cursor.execute(f"SELECT * FROM bank WHERE cid = '{CID}';")
        rows = self.cursor.fetchall()
        return rows

    def viewCart(self):
        self.cursor.execute(f"SELECT * FROM cart;")
        rows = self.cursor.fetchall()
        return rows

    def cartClear(self,bool):
        sql = (f"DELETE FROM cart WHERE oid <> {0};")
        print(sql)
        self.cursor.execute(sql)
        self.con.commit()
        if(bool):
            messagebox.showinfo(title="Video Game Pro", message="Cart data removed from database")



    def getCID(self,username,password):
        print(f"user: {username} pass: {password}")
        self.cursor.execute(f"SELECT cid FROM customer WHERE username='{username}' and password='{password}';")
        rows = self.cursor.fetchall()
        return rows

    def insert(self,title,platform, price, quantity):
        sql = (f"INSERT INTO games (title,platform, price, quantity) VALUES ('{title}', '{platform}', {price}, {quantity});")
        print(sql)
        self.cursor.execute(sql)
        self.con.commit()
        messagebox.showinfo(title="Video Game Pro", message="New game added to database")

    def insertReg(self,username,password, fName, lName, address, city, state, zip, phone, email):
        sql = (f"INSERT INTO customer (username,password, fName, lName, address, city, state, zip, phone, email) VALUES ('{username}', '{password}','{fName}','{lName}', '{address}', '{city}', '{state}', '{zip}', '{phone}', '{email}');")
        print(sql)
        self.cursor.execute(sql)
        self.con.commit()
        messagebox.showinfo(title="Video Game Pro", message="New customer added to database")

    def insertBank(self,CID, bankName, accountNumber):
        sql = (f"INSERT INTO bank (cid, bank, account) VALUES ('{CID}', '{bankName}','{accountNumber}');")
        print(sql)
        self.cursor.execute(sql)
        self.con.commit()
        messagebox.showinfo(title="Video Game Pro", message="New bank account added to database")

    def insertCart(self,GID, selectedQuantity, totalPrice):
        sql = (f"INSERT INTO cart (gid, quantity, total) VALUES ('{GID}', '{selectedQuantity}','{totalPrice}');")
        print(sql)
        self.cursor.execute(sql)
        self.con.commit()
        messagebox.showinfo(title="Video Game Pro", message="New cart item added to database")

    def removeBank(self, BID):
        sql = (f"DELETE FROM bank WHERE bid = '{BID}';")
        print(sql)
        self.cursor.execute(sql)
        self.con.commit()
        messagebox.showinfo(title="Video Game Pro", message="bank account removed from database")

    def update(self, gid, title, platform, price, quantity):
        tsql = f"UPDATE games SET title = '{title}', platform = '{platform}', price = '{price}', quantity = '{quantity}' WHERE gid = '{gid}';"
        print(tsql)
        self.cursor.execute(tsql)
        self.con.commit()
        messagebox.showinfo(title="Game Datebase", message="Game updated")

    def delete(self, gid):
        delquery = f"DELETE FROM games WHERE gid = '{gid}';"
        self.cursor.execute(delquery)
        self.con.commit()
        messagebox.showinfo(title="Game Datebase", message="Game Deleted")



def get_selected_row(event):
    global selected_tuple
    add_btn.config(state="disabled")
    try:
        index = list_box.curselection()[0]
        selected_tuple = list_box.get(index)
    except:
        index = selected_tuple[0]-1


    title_input.delete(0,'end')
    title_input.insert('end',selected_tuple[1])
    platform_combo.set(selected_tuple[2])
    price_input.delete(0,'end')
    price_input.insert('end',selected_tuple[3])
    q_input.delete(0,'end')
    q_input.insert('end',selected_tuple[4])

    #load shopping cart info
    id_input.delete(0, 'end')
    id_input.insert('end', selected_tuple[0])
    qcart_input.delete(0,'end')
    qcart_input.insert('end', 1)

def view_records():
    list_box.delete(0,'end')
    for row in db.view():
        list_box.insert('end',row)

def view_cart():
    shoppinglist_box.delete(0,'end')
    for row in db.viewCart():
        shoppinglist_box.insert('end',row)


def add_game():
    if (title_text.get() == "" or platform_combo.get() == ""):
        messagebox.showwarning(title="Error", message="Title and/or platform fields cannot be blank")
        title_input.delete(0, 'end')
        platform_combo.set('')
        price_input.delete(0, 'end')
        q_input.delete(0, 'end')
        print("returned")
        return
    else:
        db.insert(title_text.get(),platform_combo.get(), price_text.get(), q_text.get())
        list_box.delete(0,'end')
        list_box.insert('end',(title_text.get(),platform_combo.get(), price_text.get(), q_text.get()))
        title_input.delete(0,'end')
        platform_combo.set('')
        price_input.delete(0,'end')
        q_input.delete(0,'end')
        cnx.commit()

def reg_submit(win1,username, password, fName, lName, address, city, state, zip, phone, email):
    if(username =="" or password =="" or fName =="" or lName =="" or address =="" or city=="" or state =="" or zip =="" or phone =="" or email==""):
        messagebox.showerror(title="Error", message="No blank fields")
        win1.destroy()
    else:
        db.insertReg(username, password, fName,lName, address, city, state, zip, phone, email)
    # list_box.delete(0, 'end')
    # list_box.insert('end', (title_text.get(), platform_combo.get(), price_text.get(), q_text.get()))
    # title_input.delete(0, 'end')
    # platform_combo.set('')
    # price_input.delete(0, 'end')
    # q_input.delete(0, 'end')
        cnx.commit()
        win1.destroy()

def bank_insert(win2,CID, bankName, accountNumber):
    if (bankName != "" and accountNumber != ""):
        db.insertBank(CID, bankName, accountNumber)
        cnx.commit()
        loadBankData()
        win2.destroy()
    else:
        messagebox.showerror(title="Error", message="Bank name and/or account number cannot be empty.")
        win2.destroy()
        return
    # list_box.delete(0, 'end')
    # list_box.insert('end', (title_text.get(), platform_combo.get(), price_text.get(), q_text.get()))
    # title_input.delete(0, 'end')
    # platform_combo.set('')
    # price_input.delete(0, 'end')
    # q_input.delete(0, 'end')

def bank_remove(win2, BID):
    if(BID == ""):
        print("empty")
        messagebox.showerror(title="Error", message="Empty comboBox")
        win2.destroy()
        return
    else:
        BID = int(BID)
        db.removeBank(BID)
        cnx.commit()
        win2.destroy()
        loadBankData()



def delete_records():
    db.delete(selected_tuple[0])
    cnx.commit()

def clear_screen():
    list_box.delete(0,'end')
    title_input.delete(0,'end')
    platform_combo.set('')
    price_input.delete(0, 'end')
    q_input.delete(0, 'end')
    clearStartValues()

def update_records():
    db.update(selected_tuple[0],title_text.get(), platform_combo.get(), price_text.get(), q_text.get())
    title_input.delete(0, 'end')
    platform_combo.set('')
    price_input.delete(0, 'end')
    q_input.delete(0, 'end')
    cnx.commit()


def on_closing():
    cartClear(True)
    dd=db
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()
        del dd

registerOpen = False

def openRegister():

        win1 = tk.Toplevel()
        win1.geometry("300x600")
        username_label = ttk.Label(win1, text="User Name: ", background="light blue", font=("TkDefaultFont", 16))
        username_label.grid(row=1, column=0, sticky=W, pady=10, padx=3)

        username_text = StringVar()
        username_input = ttk.Entry(win1, width=10, textvariable=username_text, font=("TkDefaultFont", 12))
        username_input.grid(row=1, column=1, sticky=W)

        password_label = ttk.Label(win1, text="Password: ", background="light blue", font=("TkDefaultFont", 16))
        password_label.grid(row=2, column=0, sticky=W, pady=10, padx=3)

        password_text = StringVar()
        password_input = ttk.Entry(win1, width=10, textvariable=password_text, font=("TkDefaultFont", 12))
        password_input.grid(row=2, column=1, sticky=W)

        fName_label = ttk.Label(win1, text="First Name: ", background="light blue", font=("TkDefaultFont", 16))
        fName_label.grid(row=3, column=0, sticky=W, pady=10, padx=3)

        fName_text = StringVar()
        fName_input = ttk.Entry(win1, width=10, textvariable=fName_text, font=("TkDefaultFont", 12))
        fName_input.grid(row=3, column=1, sticky=W)

        lName_label = ttk.Label(win1, text="Last Name: ", background="light blue", font=("TkDefaultFont", 16))
        lName_label.grid(row=4, column=0, sticky=W, pady=10, padx=3)

        lName_text = StringVar()
        lName_input = ttk.Entry(win1, width=10, textvariable=lName_text, font=("TkDefaultFont", 12))
        lName_input.grid(row=4, column=1, sticky=W)

        address_label = ttk.Label(win1, text="Address: ", background="light blue", font=("TkDefaultFont", 16))
        address_label.grid(row=5, column=0, sticky=W, pady=10, padx=3)

        address_text = StringVar()
        address_input = ttk.Entry(win1, width=10, textvariable=address_text, font=("TkDefaultFont", 12))
        address_input.grid(row=5, column=1, sticky=W)

        city_label = ttk.Label(win1, text="City: ", background="light blue", font=("TkDefaultFont", 16))
        city_label.grid(row=6, column=0, sticky=W, pady=10, padx=3)

        city_text = StringVar()
        city_input = ttk.Entry(win1, width=10, textvariable=city_text, font=("TkDefaultFont", 12))
        city_input.grid(row=6, column=1, sticky=W)

        state_label = ttk.Label(win1, text="State: ", background="light blue", font=("TkDefaultFont", 16))
        state_label.grid(row=7, column=0, sticky=W, pady=10, padx=3)

        state_combo = ttk.Combobox(win1, width=8, state="readonly", font=("TkDefaultFont", 12))
        state_combo.grid(row=7, column=1, sticky=W)
        state_combo['values'] = ('AK', 'AL', 'AR', 'AS', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA', 'GU', 'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MD', 'ME', 'MI', 'MN', 'MO', 'MP', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM', 'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'PR', 'RI', 'SC', 'SD', 'TN', 'TX', 'UM', 'UT', 'VA', 'VI', 'VT', 'WA', 'WI', 'WV', 'WY'
                                    )

        zip_label = ttk.Label(win1, text="Zip Code: ", background="light blue", font=("TkDefaultFont", 16))
        zip_label.grid(row=9, column=0, sticky=W, pady=10, padx=3)

        zip_text = StringVar()
        zip_input = ttk.Entry(win1, width=10, textvariable=zip_text, font=("TkDefaultFont", 12))
        zip_input.grid(row=9, column=1, sticky=W)

        phone_label = ttk.Label(win1, text="Phone: ", background="light blue", font=("TkDefaultFont", 16))
        phone_label.grid(row=10, column=0, sticky=W, pady=10, padx=3)

        phone_text = StringVar()
        phone_input = ttk.Entry(win1, width=10, textvariable=phone_text, font=("TkDefaultFont", 12))
        phone_input.grid(row=10, column=1, sticky=W)

        email_label = ttk.Label(win1, text="Email: ", background="light blue", font=("TkDefaultFont", 16))
        email_label.grid(row=11, column=0, sticky=W, pady=10, padx=3)

        email_text = StringVar()
        email_input = ttk.Entry(win1, width=10, textvariable=email_text, font=("TkDefaultFont", 12))
        email_input.grid(row=11, column=1, sticky=W)

        submit_btn = Button(win1, text="Submit", bg="blue", fg="white", font="helvetica 10 bold", command= lambda: reg_submit(win1,username_text.get(),password_text.get(), fName_text.get(), lName_text.get(),address_text.get(), city_text.get(), state_combo.get(), zip_text.get(), phone_text.get(), email_text.get()))
        submit_btn.grid(row=12, column=1)

def grabBankData(CID): #gets bank rows
    data = db.viewBank(CID)
    return data


def openBank(bankData, CID):
    print(f"CID: {CID}")
    win2 = tk.Toplevel()
    win2.geometry("300x400")

    userCID_label = ttk.Label(win2, text=f"User: ", background="light blue", font=("TkDefaultFont", 16))
    userCID_label.grid(row=1, column=0, sticky=W, pady=10, padx=3)

    userCIDValue_label = ttk.Label(win2, text=str(CID), background="light blue", font=("TkDefaultFont", 16))
    userCIDValue_label.grid(row=1, column=1, sticky=W, pady=10, padx=3)

    list_box = Listbox(win2, height=6, font="helvetica 13", bg="light gray")
    list_box.grid(row=2, column=0, columnspan=2, sticky=W + E)

    list_box.delete(0, 'end')
    for row in bankData:
        list_box.insert('end', row)

    bankName_label = ttk.Label(win2, text="Bank Name: ", background="light blue", font=("TkDefaultFont", 16))
    bankName_label.grid(row=3, column=0, sticky=W, pady=10, padx=3)

    bankName_text = StringVar()
    bankName_input = ttk.Entry(win2, width=10, textvariable=bankName_text, font=("TkDefaultFont", 12))
    bankName_input.grid(row=3, column=1, sticky=W)

    accountNumber_label = ttk.Label(win2, text="Account Number: ", background="light blue", font=("TkDefaultFont", 16))
    accountNumber_label.grid(row=4, column=0, sticky=W, pady=10, padx=3)

    accountNumber_text = StringVar()
    accountNumber_input = ttk.Entry(win2, width=10, textvariable=accountNumber_text, font=("TkDefaultFont", 12))
    accountNumber_input.grid(row=4, column=1, sticky=W)



    submit_btn = Button(win2, text="Add", bg="green", fg="white", font="helvetica 10 bold", command=lambda: bank_insert(win2,int(CID), bankName_text.get(), accountNumber_text.get()))

    submit_btn.grid(row=5, column=1)

    bid_label = ttk.Label(win2, text="BID: ", background="light blue", font=("TkDefaultFont", 16))
    bid_label.grid(row=6, column=0, sticky=W, pady=10, padx=3)

    bid_combo = ttk.Combobox(win2, width=8, state="readonly", font=("TkDefaultFont", 12))
    bid_combo.grid(row=6, column=1, sticky=W)

    values = []  #gets all the bid values and puts them into a combobox
    for x in bankData:
        values.append(x[0])
    bid_combo['values'] = values

    remove_btn = Button(win2, text="Remove", bg="red", fg="white", font="helvetica 10 bold",
                        command=lambda: bank_remove(win2, bid_combo.get()))

    remove_btn.grid(row=7, column=1)


def enableAdminButtons():
    add_btn.config(state="normal")
    modify_btn.config(state="normal")
    delete_btn.config(state="normal")
    clr_btn.config(state="normal")

def enableUserButtons():
    bank_btn.config(state="normal")
    logout_btn.config(state="normal")
    purchase_btn.config(state="normal")
    loadHistory_btn.config(state="normal")
    clearHistory_btn.config(state="normal")

def disableAllButtons():
    add_btn.config(state="disabled")
    modify_btn.config(state="disabled")
    delete_btn.config(state="disabled")
    bank_btn.config(state="disabled")
    logout_btn.config(state="disabled")
    purchase_btn.config(state="disabled")
    clr_btn.config(state="disabled")
    loadHistory_btn.config(state="disabled")
    clearHistory_btn.config(state="disabled")

def login():
    if (username_text.get() =="" or password_text.get() == ""):
        messagebox.showwarning(title="Error", message="Username and/or password fields cannot be blank")
        print("returned")
        return
    else:
        cidrow = db.getCID(username_text.get(),password_text.get())
        username_input.delete(0, 'end')
        password_input.delete(0, 'end')
        try:
            global globalLogin
            globalLogin= cidrow[0][0]
            if (globalLogin==1):
                signedin_label.config(text=f"ADMIN: {globalLogin}")
                #admin only options
                enableAdminButtons()
                #other options
                enableUserButtons()

            else:
                signedin_label.config(text=f"USER: {globalLogin}")
                enableUserButtons()
                print(type(globalLogin))
        except:
            messagebox.showwarning(title="Error", message="No such user")

        loadBankData()

def logout():
    global globalLogin
    globalLogin = ""
    signedin_label.config(text=f"USER: {globalLogin}")
    disableAllButtons()
    print(globalLogin)

def clearTitle():
    add_btn.config(state="normal")
    title_input.delete(0, 'end')
    platform_combo.set('')
    price_input.delete(0, 'end')
    q_input.delete(0, 'end')

def modifyGame():
    tempCID = selected_tuple[0]
    tempTitle = title_text.get()
    tempPlatform = platform_combo.get()
    tempPrice = price_text.get()
    tempQ = q_text.get()
    db.update(tempCID,tempTitle, tempPlatform, tempPrice, tempQ)
    view_records()
    print(f"{tempCID} {tempTitle} {tempPlatform} {tempPrice} {tempQ}")

def cartAdd(gid, price, itemQuantity, selectedQuantity):
        global cartTotal
        if(selectedQuantity == "" or gid == ""):
            messagebox.showerror(title="Error: Cart Add input", message="Fields cannot be blank")
            return;
        else:
            print(f"gid: {gid} price: {price} itemQ: {itemQuantity} selectQ: {selectedQuantity}")
            if(itemQuantity < selectedQuantity):
                messagebox.showerror(title="Error", message="Not enough quantity in stock")
                id_input.delete(0, 'end')
                qcart_input.delete(0, 'end')
                return
            else:
                itemPrice = float(price)
                itemTotal = int(selectedQuantity) * float(itemPrice)
                cartTotal = cartTotal + itemTotal
                cartTotal = round(cartTotal,2)
                print(itemTotal)
                gTotal2_label.config(text= '$'+str(cartTotal))
                db.insertCart(gid,selectedQuantity,itemTotal)
                view_cart()
                id_input.delete(0, 'end')
                qcart_input.delete(0, 'end')

def cartClear(bool):
    db.cartClear(bool)
    shoppinglist_box.delete(0, 'end')
    id_input.delete(0, 'end')
    qcart_input.delete(0, 'end')
    global cartTotal
    cartTotal = 0.0
    gTotal2_label.config(text='$' + str(cartTotal))



def clearStartValues(): #clears some of the start values that are not blank for some reason
    price_input.delete(0, 'end')
    q_input.delete(0, 'end')
    id_input.delete(0,'end')
    qcart_input.delete(0,'end')

def loadBankData():
    bankData = grabBankData(globalLogin)
    values = []  # gets all the bid values and puts them into a combobox
    for x in bankData:
        values.append(str(x[0]) + " " + x[2] + " " + x[3])
    print(values)
    cartBank_combo['values'] = values


globalLogin = 0
cartTotal = 0.00
db = VideogameDB()

root = Tk()

root.title("Video Game Pro")
root.configure(background="light blue")
root.geometry("950x650")
root.resizable(width=False, height=False)


# Register user
username_label = ttk.Label(root, text="User Name: ", background="light blue", font=("TkDefaultFont", 16))
username_label.grid(row=1, column=0, sticky=W, pady=10, padx=3)

username_text = StringVar()
username_input = ttk.Entry(root, width=10, textvariable=username_text, font=("TkDefaultFont", 12))
username_input.grid(row=1, column=1, sticky=W)

password_label = ttk.Label(root, text="Password: ", background="light blue", font=("TkDefaultFont", 16))
password_label.grid(row=1, column=2, sticky=W, pady=10, padx=3)

password_text = StringVar()
password_input = ttk.Entry(root, width=10, textvariable=password_text, font=("TkDefaultFont", 12),show="*")
password_input.grid(row=1, column=3, sticky=W)

login_btn = Button(root, text="Login", bg="green", fg="white", font="helvetica 10 bold", command=login)
login_btn.grid(row=1, column=4)

register_btn = Button(root, text="Register", bg="purple", fg="white", font="helvetica 10 bold", command=openRegister)
register_btn.grid(row=1, column=5)

logout_btn = Button(root, text="Logout", bg="red", fg="white", font="helvetica 10 bold", state="disabled", command=logout)
logout_btn.grid(row=1, column=6)

bank_btn = Button(root, text="Bank \u2699", bg="slate gray", fg="white", font="helvetica 10 bold", command=lambda: openBank(grabBankData(globalLogin),globalLogin), state="disabled")
bank_btn.grid(row=1, column=7)

exit_btn = Button(root, text="Exit", bg="violetred", fg="white", font="helvetica 10 bold", command=on_closing)
exit_btn.grid(row=1, column=8, sticky=W)

signedin_label = ttk.Label(root, text="USER: ", background="light blue", font=("TkDefaultFont", 16))
signedin_label.grid(row=1, column=9, sticky=W, pady=10, padx=3)



# Add game to system
title_label = ttk.Label(root, text="Game Title: ", background="light blue", font=("TkDefaultFont", 16))
title_label.grid(row=2, column=0, sticky=W, pady=10, padx=3)

title_text = StringVar()
title_input = ttk.Entry(root, width=10, textvariable=title_text, font=("TkDefaultFont", 12))
title_input.grid(row=2, column=1, sticky=W)
title_input.focus()

platform_label = ttk.Label(root, text="Platform: ", background="light blue", font=("TkDefaultFont", 16))
platform_label.grid(row=2, column=2, padx=3)

platform_combo = ttk.Combobox(root, width=8, state="readonly", font=("TkDefaultFont", 12))
platform_combo.grid(row=2, column=3, sticky=W)
platform_combo['values'] = (' PS5',
                            ' PS4',
                            ' Xbox X',
                            ' Xbox One',
                            ' Switch',
                            ' PC'
                            )

price_label = ttk.Label(root, text="Price: ", background="light blue", font=("TkDefaultFont", 16))
price_label.grid(row=2, column=4, padx=3)

price_text = DoubleVar()
price_input = ttk.Entry(root, width=10, textvariable=price_text, font=("TkDefaultFont", 12))
price_input.grid(row=2, column=5, sticky=W)

q_label = ttk.Label(root, text="Quantity: ", background="light blue", font=("TkDefaultFont", 16))
q_label.grid(row=2, column=6, padx=3)

q_text = IntVar()
q_input = ttk.Entry(root, width=8, textvariable=q_text, font=("TkDefaultFont", 12))
q_input.grid(row=2, column=7, sticky=W)

clr_btn = Button(root, text="CLR", bg="red", fg="white", font="helvetica 10 bold", state="disabled", command=clearTitle)
clr_btn.grid(row=2, column=8)

add_btn = Button(root, text="Add Game", bg="blue", fg="white", font="helvetica 10 bold",state="disabled", command=add_game)
add_btn.grid(row=2, column=9)

#Item display with buttons
list_box = Listbox(root, height=16, font="helvetica 13", bg="light gray")
list_box.grid(row=3, column=0, columnspan=4, sticky=W + E)
list_box.bind('<<ListboxSelect>>',get_selected_row)

scroll_bar = Scrollbar(root)
scroll_bar.grid(row=3, column=3)

list_box.configure(yscrollcommand=scroll_bar.set)
scroll_bar.configure(command=list_box.yview)

modify_btn = Button(root, text="Modify Record", bg="purple", fg="white", font="helvetica 10 bold", state="disabled", command=modifyGame)
modify_btn.grid(row=4, column=2)

delete_btn = Button(root, text="Delete Record", bg="red", fg="white", font="helvetica 10 bold", state="disabled", command=delete_records)
delete_btn.grid(row=4, column=3)

load_btn = Button(root, text="Load Records", bg="cornflowerblue", fg="white", font="helvetica 10 bold", command=view_records)
load_btn.grid(row=4, column=0)

clear_btn = Button(root, text="Clear Screen", bg="maroon", fg="white", font="helvetica 10 bold", command=clear_screen)
clear_btn.grid(row=4, column=1, sticky=W)

# shopping cart area
cartframe = Frame(root, bg="light blue", width=150, height = 200)
cartframe.grid(row=3, column=5)

shoppinglist_box = Listbox(root, height=12, font="helvetica 13", bg="light gray")
shoppinglist_box.grid(row=3, column=6, columnspan=3, sticky= N +S)
#
cart_label = ttk.Label(cartframe, text="CART", background="light blue", font=("TkDefaultFont", 16))
cart_label.grid(row =0,column =0)

separator2 = Separator(cartframe, orient = 'horizontal')
separator2.grid(row=1,column =0, columnspan =4, sticky=" ew", pady=10)


id_label = ttk.Label(cartframe, text="GID: ", background="light blue", font=("TkDefaultFont", 14))
id_label.grid(row =2,column =0)
#
id_text = IntVar()
id_input = ttk.Entry(cartframe, width=3, textvariable=id_text, font=("TkDefaultFont", 12))
id_input.grid(row=2, column=1)
#
qcart_label = ttk.Label(cartframe, text="Q: ", background="light blue", font=("TkDefaultFont", 14))
qcart_label.grid(row=3, column=0)

qcart_text = IntVar()
qcart_input = ttk.Entry(cartframe, width=3, textvariable=qcart_text, font=("TkDefaultFont", 12))
qcart_input.grid(row=3, column=1)

clearCart_btn = Button(cartframe, text="Clear", bg="red", fg="white", font="helvetica 10 bold", command=lambda: cartClear(True))
clearCart_btn.grid(row=4, column=0, pady = 10)

addCart_btn = Button(cartframe, text="Add", bg="green", fg="white", font="helvetica 10 bold", command=lambda: cartAdd(id_input.get(),price_input.get(),q_input.get() ,qcart_input.get()))
addCart_btn.grid(row=4, column=1, pady = 10)

separator = Separator(cartframe, orient = 'horizontal')
separator.grid(row=5,column =0, columnspan =4, sticky=" ew", pady=10)

gTotal_label = ttk.Label(cartframe, text="Total:", background="light blue", font=("TkDefaultFont", 12))
gTotal_label.grid(row=6, column=0)

gTotal2_label = ttk.Label(cartframe, text="$0.0", background="light blue", font=("TkDefaultFont", 14))
gTotal2_label.grid(row=6, column=1)

selectBank_label = ttk.Label(cartframe, text="Bank: ", background="light blue", font=("TkDefaultFont", 12))
selectBank_label.grid(row=7, column=0)

cartBank_combo = ttk.Combobox(cartframe, width=4, state="readonly", font=("TkDefaultFont", 12))
cartBank_combo.grid(row=7, column=1)
cartBank_combo['values'] = 0


separator3 = Separator(cartframe, orient = 'horizontal')
separator3.grid(row=9,column =0, columnspan =4, sticky=" ew", pady=10)

purchase_btn = Button(root, text="PURCHASE", relief="raised", bd=6, bg="spring green", fg="black", font="helvetica 10 bold", state="disabled", command="")
purchase_btn.grid(row=4, column=7)

#purchase history
purchaselist_box = Listbox(root, height=9, font="helvetica 13", bg="light gray")
purchaselist_box.grid(row=5, column=0, columnspan=7,padx=5, pady=5, sticky= "E W")

purchaseFrame = Frame(root, bg="light blue", width=80, height = 200)
purchaseFrame.grid(row=5, column=7)

history_label = ttk.Label(purchaseFrame, text="History", background="light blue", font=("TkDefaultFont", 16))
history_label.grid(row=0, column=0)

separatorP1 = Separator(purchaseFrame, orient = 'horizontal')
separatorP1.grid(row=1,column =0, columnspan =4, sticky="WE", pady=10)

loadHistory_btn = Button(purchaseFrame, text="Load", bg="cornflowerblue", fg="white", font="helvetica 10 bold", state="disabled", command=modifyGame)
loadHistory_btn.grid(row=2, column=0)

clearHistory_btn = Button(purchaseFrame, text="Clear", bg="red", fg="white", font="helvetica 10 bold", state="disabled", command=modifyGame)
clearHistory_btn.grid(row=3, column=0)

separatorP2 = Separator(purchaseFrame, orient = 'horizontal')
separatorP2.grid(row=4,column =0, columnspan =4, sticky="WE", pady=10)

view_records()
clearStartValues()
cartClear(False)


root.mainloop()
