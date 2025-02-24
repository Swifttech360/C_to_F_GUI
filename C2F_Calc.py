import tkinter as tk
from tkinter import Button, PhotoImage

buttonFile = True

screen = tk.Tk()
screen.config(background= '#1f1f1f')
screen.title("C to F Calculator")
screen.geometry(f'{screen.winfo_screenwidth()}x{screen.winfo_screenheight()}')

#Entry____________________________________________________________________________________
entryField = \
    tk.Entry(screen,
    font=('arial', 20),
    justify= 'center',
    foreground= "#ebebec",
    background='grey',
    borderwidth=0
    )


entryField.pack()
entryField.place(
    relx=.5,
    rely=.46,
    anchor='e',
    width=300,
    height=40,
)

entryField.insert(0, "Enter Celsius (i.e., 25)")
clicked = False
def focusIn(event):
    global clicked
    if not clicked:
        entryField.delete(0, 'end')
        clicked = True
entryField.bind('<Button-1>', focusIn)

#__________________________________________Output Label____________________________________
outputLabel = tk.Label(
    foreground='#ebebec',
    text='Fahrenheit Output',
    font=('arial', 20,),
    
)
outputLabel.config(background='grey')
outputLabel.place(
    relx=.5,
    rely=.52,
    anchor='e',
    width=300,
    height=39
)
#__________________________________________Page Label______________________________________
pageLabel = tk.Label\
    (screen,
    font=('arial', 60),
    text='Celsius to Fahrenheit Calculator',
    background='green')
#   foreground='black'
    
pageLabel.pack()
pageLabel.place(
    relx=.5,
    rely=.28,
    anchor='center'
)
try:
    buttonImage = PhotoImage(
        file='GreenButton.png')
    buttonImage = buttonImage.subsample(10,12)
except tk.TclError:
    buttonFile=False
    
enterButton = tk.Button(screen)
#enterButton.pack()
if buttonFile:
    enterButton.config(image=buttonImage,
    bg='#1f1f1f',
    activebackground='#1f1f1f',
    borderwidth= 0,
    compound='center',
    foreground='black',
    font=('arial', 35, "bold")
    )
else:
    enterButton.config(
        background='green',
        activebackground='#00ec41',
        width=9,
        height=1,
        font=('arial', 30, "bold")
    )
    

enterButton.config(text='Convert')
enterButton.place(
    relx=.53,
    rely=.506,
    anchor='w',
)







tk.mainloop()