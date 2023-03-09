import tkinter as tk
import socket

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class UserReg:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('User Sign up')
        self.username1 = tk.StringVar()
        self.password1 = tk.StringVar()
        self.logged_in1 = False

        # Create the submit button
        submit_button1 = tk.Button(self.root, text='Submit', command=self.on_submit1)
        submit_button1.pack()

        # Create the sign up button
        signup_button1 = tk.Button(self.root, text='Sign Up', command=self.on_signup1)
        signup_button1.pack()

        # Create the status label to display login success or failure
        self.status_label1 = tk.Label(self.root, text='')
        self.status_label1.pack()

    def on_submit1(self):
        username1 = self.username1.get()
        password1 = self.password1.get()
        message1 = f'{username1},{password1}'
        response1 = self.send_message(message1)
        if response1.startswith(b'Welcome,'):
            self.logged_in = True
            self.status_label.config(text=response1.decode())
        else:
            self.status_label.config(text=response1.decode())

    def on_signup1(self):
        # Create the user registry window
        registry_window1 = tk.Toplevel(self.root)
        registry_window1.title('User Registration')

        # Create the username label and entry
        username_label1 = tk.Label(registry_window1, text='Username')
        username_label1.pack()
        username_entry1 = tk.Entry(registry_window1, textvariable=tk.StringVar())
        username_entry1.pack()

        # Create the password label and entry
        password_label1 = tk.Label(registry_window1, text='Password')
        password_label1.pack()
        password_entry1 = tk.Entry(registry_window1, textvariable=tk.StringVar(), show='*')
        password_entry1.pack()

        def on_signup_submit1():
            # Create the new user object and save it to disk
            username1 = username_entry1.get()
            password1 = password_entry1.get()
            new_user1 = User(username1, password1)
            with open('users.txt', 'a') as f:
                f.write(f'{new_user1.username1},{new_user1.password}\n')

            # Close the user registry window
            registry_window1.destroy()

        # Create the Sign Up button
        signup_button1 = tk.Button(registry_window1, text='Sign Up', command=on_signup_submit1)
        signup_button1.pack()

    def send_message(self, message):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect(('localhost', 5000))
            s.sendall(message.encode())
            response = s.recv(1024)
            return response

    def start(self):
        self.root.mainloop()

client = UserReg()
signin_window1 = tk.Toplevel()
signin_window1.title('Sign In')

# Add sign in widgets here
# ...

def on_close():
    signin_window1.destroy()

signin_window1.protocol("WM_DELETE_WINDOW", on_close) # Handle window close event

client.start()
