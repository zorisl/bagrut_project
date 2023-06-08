import threading
import tkinter
from tkinter import *
from tkinter import ttk, messagebox
from users import *

class Register(tkinter.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.geometry('600x600')
        self.title('register')
        self.userdb = User()

        self.create_gui()
        Button(self, text='Close', command=self.close).pack(expand=True, side = BOTTOM)

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


        self.buttonPlus = Button(self, text="register", command=self.handle_add_user, width=20, background="green")
        self.buttonPlus.place(x=10, y=200)

    def handle_add_user(self):
        self.client_handler = threading.Thread(target=self.register_user, args=())
        self.client_handler.daemon = True
        self.client_handler.start()

    def register_user(self):


        print("register")
        arr = ["register", self.username.get(), self.password.get()]
        str_insert = ",".join(arr)
        print(str_insert)
        self.parent.client_socket.send(str_insert.encode())
        data = self.parent.client_socket.recv(1024).decode()
        print(data)

