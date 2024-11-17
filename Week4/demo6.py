from tkinter import *
import tkinter as tk

root = Tk()
root.geometry("960x540")
heading_label=Label(root, text="Welcome To Harry Travels", bd=30, fg="red")
heading_label.config(font=('Tahoma', 14, 'bold'))
heading_label.pack()
lblName = Label(root, text="Name").place(x=40, y=80)
lblName = Label(root, text="Phone").place(x=40, y=110)
lblName = Label(root, text="Gender").place(x=40, y=140)
lblName = Label(root, text="Emergency Contact").place(x=40, y=170)
lblName = Label(root, text="Payment Mode").place(x=40, y=200)

e1=Entry(root).place(x=200, y=80)
e2=Entry(root).place(x=200, y=110)
e3=Entry(root).place(x=200, y=140)
e4=Entry(root).place(x=200, y=170)
e5=Entry(root).place(x=200, y=200)

# c1 = tk.Checkbutton(window, text='Python',variable=var1, onvalue=1, offvalue=0, command=print_selection)
# c1.pack()

root.mainloop()