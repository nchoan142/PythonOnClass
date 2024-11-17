from tkinter import *
import tkinter as tk

window_parent = tk.Tk()
window_parent.geometry("300x200")

frame1 = tk.Frame(master=window_parent, height=80, bg="red")
frame1.pack(fill=tk.X)

frame2 = tk.Frame(master=window_parent, height=50, bg="yellow")
frame2.pack(fill=tk.X)

frame3 = tk.Frame(master=window_parent, height=40, bg="blue")
frame3.pack(fill=tk.X)

window_parent.mainloop()