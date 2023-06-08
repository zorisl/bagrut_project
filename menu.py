import threading
import tkinter
from tkinter import *
from add_users import Register
from login import Login
import socket
from tkinter import Tk
class App(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('300x200')
        self.title('Main Window')
        # place a button on the root window
        self.btn_register = Button(self, text='Register', command=self.open_register)
        self.btn_register.place(x=50, y=50)

        self.btn_login = Button(self, text='Login', command=self.open_login)
        self.btn_login.place(x=50, y=100)
        self.handle_thread_socket()

    def open_register(self):
        window = Register(self)
        window.grab_set()
        self.withdraw()

    def open_login(self):
        window = Login(self)
        window.grab_set()
        self.withdraw()
    def handle_thread_socket(self):
        client_handler = threading.Thread(target=self.create_socket, args=())
        client_handler.daemon = True
        client_handler.start()

    def create_socket(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect(('127.0.0.1', 1802))
        data = self.client_socket.recv(1024).decode()
        print("data"+data)
        print("hi", self.client_socket)

if __name__ == "__main__":
    app = App()
    app.mainloop()