# installed required libraries
from tkinter import *
from string import ascii_uppercase
import random
from tkinter import messagebox
import pyglet
from pyglet import *
from pyglet.gl import *

# show window
window = Toplevel()
window.title("PYTHON | RETRO HANGMAN")
width = window.winfo_screenwidth()
height = window.winfo_screenheight()
x = int(width / 2 - 500 / 2)
y = int(height / 2 - 500 / 2)
str1 = "594x399+" + str(x) + "+" + str(y)
window.geometry('5000x5000')
img =PhotoImage(file="C:\PyProjects\RCAP\imgrethang\hangmanbg.png")
img=img.subsample(2)
label = Label(window, image=img, bg='#010FFD', height=0, width=0)
label.place(x=700, y=400, anchor= "n")
window['background']= '#010FFD'
label.image=img

#able the resize of the window
window.resizable(width=True, height=True)


# customize arcade font

pyglet.font.add_file("C:/PyProjects/RCAP/imgrethang/ka1.ttf")
customfont = pyglet.font.load("Karmatic Arcade")


# list of words

global word_list

word_list = [ "HANGMAN", "ARCADE", "GAMING", "VINTAGE", "RETRO", "PYTHON", "HACKCADE", "COMMUNITY", "PLAYABLE", "POLYGON", "WITCHCRAFT", "GENESIS", "INVADER", "CLASSICS", "PUZZLE", "VERSION", "NINTENDO"]




# images to create dashes for each wrong guess
global photos
global i
photos = [PhotoImage(file="C:\PyProjects\RCAP\imgrethang\hang0.png"), PhotoImage(file="C:\PyProjects\RCAP\imgrethang\hang1.png"), PhotoImage(file="C:\PyProjects\RCAP\imgrethang\hang2.png"), PhotoImage(file="C:\PyProjects\RCAP\imgrethang\hang3.png"), PhotoImage(file="C:\PyProjects\RCAP\imgrethang\hang4.png"), PhotoImage(file="C:\PyProjects\RCAP\imgrethang\hang5.png") ]
for i in photos:
    i=i.subsample(2)


global img_label
img_label=Label(window)
img_label.grid(row=0, column=20, columnspan=6, padx=10, pady=40)
img_label.config(image=photos[0], height=260, width=225)


# create alphabet from A to Z
global n
n = 0
global c
for c in ascii_uppercase:
    Button(window, bg= '#FFFF66', text=c, command=lambda c=c: guess(c), font= ('Karmatic Arcade', 16), width=5).grid(row= 180 + (n // 9), column=(n % 9)+ 550, sticky= "ew")
    n += 1
Button(window,bg='#90EE90', text="New \n Game", command=lambda: newgame(), font=("Helvetica 8 bold")).grid(row=182, column=558, sticky="nsew")


# create newgame function to start a new game
global newgame
def newgame():
    global the_word_withSpaces
    global numberOfGuesses
    global label_word
    numberOfGuesses = 0
    img_label.config(image=photos[0], height=260, width=225)
    img_label.image= photos[0]
    the_word = random.choice(word_list)
    the_word_withSpaces = " ".join(the_word)
    label_word.set(" ".join("_" * len(the_word)))

# create the guess function for guessing each letter.
global guess
def guess(letter):
    global numberOfGuesses
    global guessed
    global z
    if numberOfGuesses < 5:
        txt = list(the_word_withSpaces)
        guessed = list(label_word.get())
        if the_word_withSpaces.count(letter) > 0:
            for z in range(len(txt)):
                if txt[z] == letter:
                    guessed[z] = letter
                label_word.set("".join(guessed))
                if label_word.get() == the_word_withSpaces:
                    messagebox.showinfo("RETRO HANGMAN", "Kudos! You won the Game.")
                    newgame()
        else:
            numberOfGuesses += 1
            img_label.config(image=photos[numberOfGuesses])
            img_label.image= photos[numberOfGuesses]
            if numberOfGuesses == 5:
                messagebox.showwarning("RETRO HANGMAN", "Sorry, Game Over. Better luck, next time! ")
                newgame()




label_word = StringVar()
label1= Label(window, textvariable=label_word, font= ('Karmatic Arcade', 12 ))
label1.grid(row=0, column=500, columnspan=6, padx=20, sticky= "")



newgame()
window.mainloop()
