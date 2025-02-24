import tkinter as tk
screen = tk.Tk()
screen.config(background= '#1f1f1f')
screen.title("C to F Calculator")
screen.geometry(f'{screen.winfo_screenwidth()}x{screen.winfo_screenheight()}')


entryField = \
    tk.Entry(screen,
    font=('arial', 30),
    foreground= "blue"
    )

entryField.config(background='grey')
entryField.pack()
entryField.place(relx=.5, rely=.46, anchor='center')

cLabel = tk.Label\
    (screen,
    font=('arial', 25),
    text='Celsius Input:')
cLabel.pack()
cLabel.place(
    relx=.5,
    rely=.42,
    anchor='center'
)


tk.mainloop()