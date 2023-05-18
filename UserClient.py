import tkinter as tk
import socket

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class UserClient:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('User Login')
        self.username = tk.StringVar()
        self.password = tk.StringVar()
        self.logged_in = False

        # Create the username label and entry widget
        username_label = tk.Label(self.root, text='Username:')
        username_label.pack()
        self.username_entry = tk.Entry(self.root, textvariable=self.username)
        self.username_entry.pack()

        # Create the password label and entry widget
        password_label = tk.Label(self.root, text='Password:')
        password_label.pack()
        self.password_entry = tk.Entry(self.root, show='*', textvariable=self.password)
        self.password_entry.pack()

        # Create the submit button
        submit_button = tk.Button(self.root, text='Submit', command=self.on_submit)
        submit_button.pack()

        # Create the sign in button
        signin_button = tk.Button(self.root, text='Sign Up', command=self.on_signin)
        signin_button.pack()

        # Create the status label to display login success or failure
        self.status_label = tk.Label(self.root, text='')
        self.status_label.pack()

    def on_submit(self):
        username = self.username.get()
        password = self.password.get()
        message = f'{username},{password}'
        response = self.send_message(message)
        if response.startswith(b'Welcome,'):
            self.logged_in = True
            self.status_label.config(text=response.decode())
        else:
            self.status_label.config(text=response.decode())

    def on_signin(self):
        self.root.withdraw() # Hide the login window
        signin_window = tk.Toplevel(self.root)
        signin_window.grab_set() # Grab focus to the new window

        # Add registration widgets here
        # ...
        # Create the username label and entry widget
        name_label = tk.Label(self.root, text='Username:')
        name_label.pack()
        self.name_entry = tk.Entry(self.root, textvariable=self.username)
        self.name_entry.pack()

        # Create the password label and entry widget
        password1_label = tk.Label(self.root, text='Password:')
        password1_label.pack()
        self.password1_entry = tk.Entry(self.root, show='*', textvariable=self.password)
        self.password1_entry.pack()


        # Create the sign up button
        signup_button = tk.Button(self.root, text='Sign Up', command=self.on_signup)
        signup_button.pack()

        def on_signup():
            # Create the new user object and save it to disk
            username = name_label.get()
            password = password1_label.get()
            new_user1 = User(username, password)
            with open('users.txt', 'a') as f:
                f.write(f'{username.username},{username.password}\n')
            signin_window.grab_release() # Release focus from the new window
            signin_window.destroy() # Destroy the new window
            self.root.deiconify() # Show the login window again

        def on_close():
            signin_window.grab_release() # Release focus from the new window
            signin_window.destroy() # Destroy the new window
            self.root.deiconify() # Show the login window again

        signin_window.protocol("WM_DELETE_WINDOW", on_close) # Handle window close event

    def send_message(self, message):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect(('localhost', 5000))
            s.sendall(message.encode())
            response = s.recv(1024)
            return response

    def start(self):
        self.root.mainloop()

client = UserClient()
client.start()
