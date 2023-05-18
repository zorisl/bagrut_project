import tkinter as tk
from tkinter import NW

root = tk.Tk()
canvas = tk.Canvas(root, width = 200, height = 200)
canvas.pack()
img = tk.PhotoImage(file=r'piece\wQueen.png')
canvas.create_image(20, 20, anchor=NW, image=img)
tk.mainloop()