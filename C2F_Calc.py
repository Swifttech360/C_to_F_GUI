"""
Program Name: C to F Calculator
Author: Miles Butler
Publish Date: 2/24/2024
Overview:
    This is a python program that uses a Tkinter GUI to display a program with two text boxes and a button.
    Using the simple interface, the user can enter a Celsius temperature as a floating point number in the top entry
    field. After hitting the "ºC to F" button, the program will convert the entered Cº temperature into it's
    Fahrenheit equivalent, displaying that number in the output label.
    Clicking the "ºF to ºC button will do the opposite, converting the user input from Fahrenheit to Celsius.
"""


import tkinter as tk

from tkinter import PhotoImage

def numFormatter(num):
    """
    :param num: A floating point number
    :return: num, formated down to four decimal points and stripped of all trailing zeros and decimal points.
    """
    return f"{num:.4f}".rstrip("0").rstrip(".")

def CtoF_ButtonClick():
    """
    Gets the Celsius input from the entry field, then converts
    that number to Fahrenheit before displaying it in the outputLabel.
    :return:None
    """
    fullTextString = entryField.get()
    fullTextString= fullTextString.rstrip("ºC")
    strippedEntryString= fullTextString.rstrip("ºF")
    entryField.delete(0, 'end')
    entryField.insert(0, strippedEntryString)
    celsius = entryField.get()
    try:
        fahrenheit = 9/5 * float(celsius) + 32
    except ValueError:
        outputLabel.config(text="Invalid Input", foreground='#8B0000', font=('arial', 23, 'bold'))
        print('Invalid Input\nMake sure only numbers are entered in the entry field.')
        return None
    fahrenheit = numFormatter(fahrenheit)
    outputLabel.config(text=f"{fahrenheit}ºF", foreground='#ebebec', background='red', font=('arial', 20))
    entryField.config(background='blue')
    entryField.insert('end', 'ºC')
    

def FtoC_ButtonClick():
    """
    Gets the Fahrenheit input from the entry field, then converts
    that number to Celsius before displaying it in the outputLabel.
    :return:None
    """
    fullTextString = entryField.get()
    fullTextString= fullTextString.rstrip("ºC")
    strippedEntryString= fullTextString.rstrip("ºF")
    entryField.delete(0, 'end')
    entryField.insert(0, strippedEntryString)
    fahrenheit = entryField.get()
    try:
        celsius = (float(fahrenheit) - 32) / 1.8
    except ValueError:
        outputLabel.config(text="Invalid Input", foreground='#8B0000', font=('arial', 23, 'bold'))
        print('Invalid Input\nMake sure only numbers are entered in the entry field.')
        return None
    celsius = numFormatter(celsius)
    outputLabel.config(text=f"{celsius}ºC", foreground='#ebebec', background='blue', font=('arial', 20),)
    entryField.config(background='red')
    entryField.insert('end', 'ºF')

def focusIn(event):
    global outputLabel
    global entryField
    entryField.config(bg='grey')
    outputLabel.config(bg='grey')
    global clicked
    if not clicked:
        entryField.delete(0, 'end')
        clicked = True

buttonFile = True

screen = tk.Tk()
screen.config(background= '#1f1f1f')
screen.title("C to F Calculator")
screen.geometry(f'{screen.winfo_screenwidth()}x{screen.winfo_screenheight()}')

#_____________________________________EntryField______________________________________
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
    anchor='center',
    width=300,
    height=47,
)

entryField.insert(0, "Celsius Input (i.e., 25)")
clicked = False

entryField.bind('<Button-1>', focusIn)

#__________________________________________OutputLabel____________________________________
outputLabel = tk.Label(
    foreground='#ebebec',
    text='Fahrenheit Output',
    font=('arial', 20),
    
)
outputLabel.config(background='grey')
outputLabel.place(
    relx=.5,
    rely=.565,
    anchor='center',
    width=300,
    height=46
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
        file='darkGreenButtonOFF.png') # Allows user to add in images as needed by removing "OFF",
                                    # but I decided to not use the one I made.
    buttonImage = buttonImage.subsample(10,12)
except tk.TclError:
    buttonFile=False
#_________________________C2F_Button_________________________
C2F_Button = tk.Button(screen)
#enterButton.pack()
if buttonFile:
    C2F_Button.config(image=buttonImage,
    bg='#1f1f1f',
    activebackground='#1f1f1f',
    borderwidth= 0,
    compound='center',
    foreground='black',
    font=('arial', 35, "bold")
    )
else:
    C2F_Button.config(
        background='green',
        activebackground='#00ec41',
        #width=9,
        #height=1,
        font=('arial', 27, "bold")
    )
    

C2F_Button.config(
    text='ºC to ºF',
    command=CtoF_ButtonClick
)
C2F_Button.place(
    relx=.349,
    rely=.5155,
    width=226,
    height=81,
    anchor='w',
)

#______________________________F2C_Button______________________________
F2C_Button = tk.Button(
    background='green',
    foreground='black',
    font=('arial', 27, 'bold'),
    text='ºF to ºC',
    command=FtoC_ButtonClick
)
F2C_Button.place(
    
    relx=.565,
    rely=.5155,
    width=226,
    height=81,
    anchor='w'
)


#___________________________Equal Label________________________________
equal = tk.Label(
    bg=screen['bg'],
    borderwidth=0,
    text='=',
    font=('arial', 55, 'bold'),
    foreground= 'white'
)
equal.place(
    relx=.5,
    rely=.5155,
    anchor='center'
)

tk.mainloop()