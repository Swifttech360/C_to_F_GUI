import tkinter as tk
from tkinter import mainloop

root = tk.Tk()
exampleEntry = tk.Entry(root)
exampleEntry.insert(0, "some text")

def some_callback(event): # note that you must include the event as an arg, even if you don't use it.
    exampleEntry.delete(0, "end")
    return None
B = tk.Entry(root)
B.place(relx=.5, rely=.5, anchor='center')
exampleEntry.bind("<Button-1>", some_callback)

exampleEntry.pack()
mainloop()