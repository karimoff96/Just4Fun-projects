from tkinter import *
import random
import pandas

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}
try:
    data = pandas.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    origin = pandas.read_csv("data/data.csv")
    to_learn = origin.to_dict(orient='records')
else:
    to_learn = data.to_dict(orient='records')


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text='Korean', fill='black')
    canvas.itemconfig(card_word, text=current_card["Korean"], fill='black')
    canvas.itemconfig(canvas_background, image=card_front)
    flip_timer = window.after(5000, func=flip_card)


def flip_card():
    canvas.itemconfig(canvas_background, image=card_back)
    canvas.itemconfig(card_title, text='English', fill='white')
    canvas.itemconfig(card_word, text=current_card["English"], fill='white')


def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv('data/words_to_learn.csv', index=False)
    next_card()


window = Tk()
window.title('Flashy')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(5000, func=flip_card)

canvas = Canvas(width=800, height=526)
card_front = PhotoImage(file='images/card_front.png')
card_back = PhotoImage(file='images/card_back.png')

canvas_background = canvas.create_image(400, 263, image=card_front)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

card_title = canvas.create_text(400, 150, text="Title", fill="black", font=('Ariel', 40, "italic"))
card_word = canvas.create_text(400, 263, text="Word", fill="black", font=('Ariel', 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

right_image = PhotoImage(file='images/right.png')
right_button = Button(image=right_image, highlightthickness=0, command=is_known)
right_button.grid(column=1, row=1)
next_card()

wrong_image = PhotoImage(file='images/wrong.png')
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)

window.mainloop()
