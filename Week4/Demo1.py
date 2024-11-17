from tkinter import *
import tkinter as tk

window_parent = tk.Tk()
window_parent.geometry("300x200")

frame1 = tk.Frame(master=window_parent, width=100, height=100, bg="orange")
frame1.pack()

frame2 = tk.Frame(master=window_parent, width=50, height=50, bg="blue")
frame2.pack()

frame3 = tk.Frame(master=window_parent, width=25, height=25, bg="orange")
frame3.pack()

window_parent.mainloop()