import tkinter as tk

def on_entry_click(event):
    """Clears the entry when the user clicks inside if it contains the default text."""
    if entry.get() == default_text:
        entry.delete(0, tk.END)
        entry.config(fg="black")  # Change text color

def on_focus_out(event):
    """Restores default text if the entry is left empty."""
    if not entry.get():
        entry.insert(0, default_text)
        entry.config(fg="gray")

root = tk.Tk()
root.title("Tkinter Entry Placeholder")

default_text = "Enter your text here..."
entry = tk.Entry(root, fg="gray")
entry.insert(0, default_text)

entry.bind("<FocusIn>", on_entry_click)
entry.bind("<FocusOut>", on_focus_out)

entry.pack(pady=10)

B = tk.Entry(root)

B.pack()
B.place(relx=.5, rely=.5, anchor='center')
C = tk.Button(background='orange', text='Focus Out')
C.pack()
C.place(
    relx=.5,
    rely=.5)


root.mainloop()
