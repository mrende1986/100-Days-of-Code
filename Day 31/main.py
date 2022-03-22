from tkinter import *
from tkinter import messagebox
from turtle import xcor, ycor
import pyperclip
import json
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

# ---------------------------- Data for Flash Cards ------------------------------- #
import pandas

try:
    data = pandas.read_csv("Day 31/data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv('Day 31/data/french_words.csv')
    to_learn = original_data.to_dict(orient='records')
else:
    to_learn = data.to_dict(orient='records')


# ---------------------------- Random Flash Cards ------------------------------- #
from random import choice, randint, shuffle

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(to_learn)
    canvas.itemconfig(card_title, text='French',fill='black')
    canvas.itemconfig(card_word, text = current_card['French'],fill='black')
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000,func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text='English', fill = 'white')
    canvas.itemconfig(card_word, text = current_card['English'], fill='white')
    canvas.itemconfig(card_background, image = card_back_img)

def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv('Day 31/data/words_to_learn.csv',index=False)
    
    next_card()

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Flashly")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, heigh=526)
card_front_img = PhotoImage(file="Day 31/images/card_front.png")
card_back_img = PhotoImage(file="Day 31/images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400,150, text='Title', font=('Ariel', 40, 'italic'), fill="black")
card_word = canvas.create_text(400,263, text='word', font=('Ariel', 60, 'bold'), fill = 'black')
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file = 'Day 31/images/wrong.png')
unknown_button = Button(image=cross_image,command=next_card)
unknown_button.grid(row=1,column=0)

check_image = PhotoImage(file = 'Day 31/images/right.png')
known_button = Button(image=check_image,command=is_known)
known_button.grid(row=1,column=1)

next_card()

window.mainloop()