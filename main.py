from tkinter import *
import pandas as pd
from random import *

BACKGROUND_COLOR = "#B1DDC6"
FONTNAME = 'Arial'
select_word = {}
learn_dict = {}

try:
    data = pd.read_csv('./data/words_to_learn.csv')
except FileNotFoundError:
    original_data = pd.read_csv('./data/spanish_words1000.csv')
    learn_dict = original_data.to_dict(orient='records')
else:
    learn_dict = data.to_dict(orient='records')

#----------------------------Save Your Progress-------------------------------#
def is_known():
    global select_word
    next_card()
    learn_dict.remove(select_word)
    new_data = pd.DataFrame(learn_dict, columns=['Spanish', 'English'])
    new_data.to_csv('./data/words_to_learn.csv', index=False)

#----------------------------Create New Flash Cards----------------------------#
def next_card():
    global select_word, timer
    window.after_cancel(timer)
    select_word = choice(learn_dict)
    select_es = select_word['Spanish']
    canvas.itemconfig(title, text='Spanish')
    canvas.itemconfig(word, text=select_es)
    canvas.itemconfig(card_background, image=card_front)
    timer = window.after(3000, func=flip_card)


#---------------------------Flip the card-------------------------------------#
def flip_card():
    global select_word
    select_en = select_word['English']
    canvas.itemconfig(title, text='English')
    canvas.itemconfig(word, text=select_en)
    canvas.itemconfig(card_background, image=card_back)


#----------------------------Create the UI-------------------------------------#
window = Tk()
window.title('Flashy')
window.config(padx=50, pady=50,
              bg=BACKGROUND_COLOR)
timer = window.after(3000, func=flip_card)

card_front = PhotoImage(file='./images/card_front.png')
card_back = PhotoImage(file='./images/card_back.png')
right = PhotoImage(file='./images/right.png')
wrong = PhotoImage(file='./images/wrong.png')


canvas = Canvas(width=800, height=526)
card_background = canvas.create_image(400, 263, image=card_front)
canvas.config(background=BACKGROUND_COLOR,
              highlightbackground=BACKGROUND_COLOR)
canvas.grid(column=0, row=0, columnspan=2)

title = canvas.create_text(400, 150, text='Title',
                   font=(FONTNAME, 40, 'italic'))

word = canvas.create_text(400, 253, text='Word',
                   font=(FONTNAME, 60, 'bold'))


right_button = Button(image=right,
                      highlightbackground=BACKGROUND_COLOR,
                      highlightthickness=0,
                      command=is_known)
right_button.grid(column=1, row=1)
wrong_button = Button(image=wrong,
                      highlightbackground=BACKGROUND_COLOR,
                      highlightthickness=0,
                      command=next_card)
wrong_button.grid(column=0, row=1)

next_card()

window.mainloop()



