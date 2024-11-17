import tkinter as tk

root = tk.Tk()
root.geometry("400x300")

frame=tk.Frame(root, height=200, width=200, bg="limegreen")
frame.place(x=50, y=50)
label=tk.Label(frame, text="height=100\nwidth=100\n\nframe is\n200x200")
label.place(height=100, width=100, relx=0.5, rely=0.5, anchor=tk.CENTER)

root.mainloop()