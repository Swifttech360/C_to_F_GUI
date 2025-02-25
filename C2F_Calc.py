"""
Program Name: C to F Calculator
Author: Miles Butler
Publish Date: 2/24/2024
Overview:
    This is a python program that uses a Tkinter GUI to display a program with two text boxes and a button.
    Using the simple interface, the user can enter a Celsius temperature as a floating point number in the top entry
    field. After hitting the "Convert" button, the program will convert the entered Cº temperature into it's
    Fahrenheit equivalent, displaying that number in the output label.
"""


import tkinter as tk
from sys import exception
from tkinter import Button, PhotoImage

def numFormatter(num):
    """
    :param num: A floating point number
    :return: num, formated down to four decimal points and stripped of all trailing zeros and decimal points.
    """
    return f"{num:.4f}".rstrip("0").rstrip(".")

def convertButtonClick():
    """
    Gets the Celsius input from the entry field, then converts
    that number to Fahrenheit before displaying it in the outputLabel.
    :return:None
    """
    fullTextString = entryField.get()
    fullTextString= fullTextString.rstrip("ºC")
    entryField.delete(0, 'end')
    entryField.insert(0, fullTextString)
    celsius = entryField.get()
    try:
        fahrenheit = 9/5 * float(celsius) + 32
    except ValueError:
        outputLabel.config(text="Invalid Input", foreground='#8B0000', font=('arial', 23, 'bold'))
        print('Invalid Input\nMake sure only numbers are entered in the entry field.')
        return None
    fahrenheit = numFormatter(fahrenheit)
    outputLabel.config(text=f"{fahrenheit}ºF", foreground='#ebebec', font=('arial', 20))
    entryField.insert('end', 'ºC')
    

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

entryField.insert(0, "Celsius Input (i.e., 25)")
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
    font=('arial', 20),
    
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
        file='darkGreenButton.png')
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
    

enterButton.config(
    text='Convert',
    command=convertButtonClick
)
enterButton.place(
    relx=.53,
    rely=.506,
    anchor='w',
)

tk.mainloop()