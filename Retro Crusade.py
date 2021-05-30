# Building the interface

# Import module
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from time import *
import random
import os, sys

# Create object
window = Tk()
window.title("RETRO CRUSADE")

# Able the resize of the window
window.resizable(width=True, height=True)

# Adjust size
window.geometry("740x740")


# Add image file
bg =  PhotoImage(file = "C:\img_retro_crusade_bg\imgretrocrusaderevised.png")
image1= Image.open("C:\img_retro_crusade_bg\imgspaceshooter.png")
image2= Image.open("C:\img_retro_crusade_bg\imgretrohangman.png")

# Resizing the images on buttons
photo1= image1.resize((310, 190), Image.ANTIALIAS)
photo2= image2.resize((310, 190), Image.ANTIALIAS)

photoimage1=ImageTk.PhotoImage(photo1)
photoimage2=ImageTk.PhotoImage(photo2)

# Create Canvas

canvas1 = Canvas( window,bg= "black", width = 10000, height = 10000)
canvas1.pack(fill = "both", expand = True)


#Display image    

canvas1.create_image( 120, -1, image=bg, anchor = "nw")

# Opening the game

def RetroHangman():
    exec(open('C:/PyProjects/RCAP/retrohangman.py').read())

def SpaceShoot():
    exec(open('C:/PyProjects/RCAP/spaceshooter.py').read())


# Add Text 
canvas1.create_text( 730, 205, fill= "cyan", text = "   Welcome, Player. HAPPY ARCADING!")

# Create Buttons
button1 = Button( window, image = photoimage1, height=180, width=300, command = SpaceShoot)
button2 = Button( window, image = photoimage2, height=180, width=300, command = RetroHangman)
button3 = Button( window, text = "Exit", command= window.destroy)

# Display Buttons
button1_canvas = canvas1.create_window( 500, 330, anchor = "center", window = button1)

button2_canvas = canvas1.create_window( 995, 330, anchor = "center", window = button2)

button3_canvas = canvas1.create_window( 745, 700, anchor = "center", window = button3)


# Execute tkinter
window.mainloop()
