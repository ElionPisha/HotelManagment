from tkinter import *
from tkinter import messagebox
from django.http import response
import requests
import json


URL = 'http://127.0.0.1:8000/'


def retrieve_list():
    if token_out:
        headers = {
            'Authorization': f'Token {token_out}'
        }
        r = requests.get(URL+'api/', headers=headers)
        out_data = json.loads(r.text)
        data = []
        for out in out_data:
            res = out.values()
            data.append(list(res))
        for k in data:
            room_list.insert(END, k)


def login():
    global token_out
    username = username_entry.get()
    password = password_entry.get()
    print(username, password)
    if username == '' or password == '':
        messagebox.showerror(
            'Required Field', 'Username/password should not be empty')
    else:
        data = {
            "username": username,
            "password": password
        }
        try:
            response = requests.post(URL+'api-token-auth/', data=data)
            response_dict = json.loads(response.text)
            print(response_dict)
            token_out = response_dict['token']
            print(token_out)
        except Exception as e:
            messagebox.showerror(
                'Login Failure', 'Username/Credientials Invalid. Please try again!')
        retrieve_list()


def select_item(event):
    print(event)
    selection = event.widget.curselection()
    if selection:
        index = selection[0]
        data = event.widget.get(index)
        print(data)    


def clear_form():
    room_entry.delete(0, END)
    guest_entry.delete(0, END)
    check_in_entry.delete(0, END)
    check_out_entry.delete(0, END)


app = Tk()

#Username & Password
username_text = StringVar()
username_label = Label(app, text='Username', fg='red',
                       font=('bold', 10), padx=20)
username_label.grid(row=0, column=8, sticky=W)
username_entry = Entry(app, textvariable=username_text)
username_entry.grid(row=0, column=9)

password_text = StringVar()
password_label = Label(app, text='Passwod', fg='red',
                       font=('bold', 10), padx=20)
password_label.grid(row=1, column=8, sticky=W)
password_entry = Entry(app, show="*", textvariable=password_text)
password_entry.grid(row=1, column=9)


# Room
room_text = StringVar()
room_label = Label(app, text='Room On', font=('bold', 14), pady=20)
room_label.grid(row=0, column=0, sticky=W)
room_entry = Entry(app, textvariable=room_text)
room_entry.grid(row=0, column=1)

# Guest
guest_text = StringVar()
guest_label = Label(app, text='Guest', font=('bold', 14))
guest_label.grid(row=0, column=2, sticky=W)
guest_entry = Entry(app, textvariable=guest_text)
guest_entry.grid(row=0, column=3)


# Check In Date
check_in_text = StringVar()
check_in_label = Label(app, text='Check in Date', font=('bold', 14))
check_in_label.grid(row=1, column=0, sticky=W)
check_in_entry = Entry(app, textvariable=check_in_text)
check_in_entry.grid(row=1, column=1)


# #Check Out Date
check_out_text = StringVar()
check_out_label = Label(app, text='Check Out Date', font=('bold', 14))
check_out_label.grid(row=1, column=2, sticky=W)
check_out_entry = Entry(app, textvariable=check_out_text)
check_out_entry.grid(row=1, column=3)

# Room Details (List Box)
room_list = Listbox(app, height=8, width=50, border=1)
room_list.grid(row=2, column=0, columnspan=3, rowspan=6, pady=20, padx=20)

scrollbar = Scrollbar(app)
scrollbar.grid(row=3, column=3)

room_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=room_list.yview)

room_list.bind('<<ListboxSelect>>', select_item)

login_btn = Button(app, text='Login', fg='red', width=15, command=login)
login_btn.grid(row=2, column=9, pady=20)

add_btn = Button(app, text='Add Room', width=15)
add_btn.grid(row=3, column=9)

remove_btn = Button(app, text='Delete Room', width=15)
remove_btn.grid(row=4, column=9)

update_btn = Button(app, text='Update Room', width=15)
update_btn.grid(row=5, column=9)

clear_btn = Button(app, text='Clear', width=15, command=clear_form)
clear_btn.grid(row=6, column=9)


app.title('Hotel Maanagement')
app.geometry('750x350')

app.mainloop()
