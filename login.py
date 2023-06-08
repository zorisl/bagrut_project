import threading
import tkinter
from tkinter import *
from add_users import Register
import socket

class Login(tkinter.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.geometry('300x100')
        self.title('Toplevel Window 2')


        Button(self, text='Close', command=self.close).pack(expand=True)

    def create_gui(self):
        # phase 1 button
        self.lbl_username = Label(self, width=10, text="email :")
        self.lbl_username.place(x=10, y=50)
        self.username = Entry(self, width=20)
        self.username.place(x=100, y=50)

        self.lbl_password = Label(self, width=10, text="password :")
        self.lbl_password.place(x=10, y=100)
        self.password = Entry(self, width=20)
        self.password.place(x=100, y=100)

        self.buttonPlus = Button(self, text="register", command=self.handle_login_user, width=20, background="green")
        self.buttonPlus.place(x=10, y=200)

    def handle_login_user(self):
        self.client_handler = threading.Thread(target=self.login_user, args=())
        self.client_handler.daemon = True
        self.client_handler.start()

    def login_user(self):
        print("login")
        arr = ["login", self.username.get(), self.password.get()]
        str_insert = ",".join(arr)
        print(str_insert)
        self.parent.client_socket.send(str_insert.encode())
        data = self.parent.client_socket.recv(1024).decode()
        print(data)

    def close(self):
        self.parent.deiconify()
        self.destroy()