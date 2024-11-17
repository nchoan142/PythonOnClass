import tkinter as tk

window_parent = tk.Tk()
window_parent.geometry("300x200")

label1 = tk.Label(
    window_parent,
    text='Box 1',
    bg='red',
    fg='white'
)

label1.pack(
    ipadx=10,
    ipady=10,
    fill='x'
)

label2 = tk.Label(
    window_parent,
    text='Box 2',
    bg='green',
    fg='white'
)

label2.pack(
    ipadx=10,
    ipady=10,
    fill='x'
)

label3 = tk.Label(
    window_parent,
    text='Box 3',
    bg='blue',
    fg='white'
)

label3.pack(
    ipadx=10,
    ipady=10,
    fill='x'
)

label4 = tk.Label(
    window_parent,
    text='Left',
    bg='cyan',
    fg='black'
)

label4.pack(
    ipadx=10,
    ipady=10,
    expand=True,
    fill='both',
    side='left'
)

label5 = tk.Label(
    window_parent,
    text='Center',
    
    bg='magenta',
    fg='black'
)

label5.pack(
    ipadx=10,
    ipady=10,
    expand=True,
    fill='both',
    side='left'
)

label6=tk.Label(
    window_parent,
    text='Right',
    bg="yellow",
    fg="black"
)

label6.pack(
    ipadx=10,
    ipady=10,
    expand=True,
    fill='both',
    side='left'
)

window_parent.mainloop()