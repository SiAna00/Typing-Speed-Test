from tkinter import *
import random
import time
from text import words

def generate_words():
    random_words = random.choices(words, k=50)
    words_label = Label(window, bg="bisque", text=random_words, font="helvetica 16", wraplength=530, pady=20, padx=20)
    words_label.grid(column=2, row=2, columnspan=2)
    

def count_wpm():
    user_input = input_field.get("1.0", END)
    user_words = user_input.split()

    # Count how many words per minute
    wpm = len(user_words)
    intro_label.config(text=f"Your typing speed is {wpm} WPM.")


def start_typing():
    global input_field

    # Create user input field
    input_field = Text(window, bg="bisque", width=70, height=10)
    input_field.grid(column=2, row=4, columnspan=2, padx=20, pady=20)

    # Count time (1 minute)
    window.after(10000, count_wpm)


# Create GUI with Tkinter
window = Tk()
window.title("Typing Speed Test")
window.configure(bg="SlateBlue2", padx=20, pady=20)

intro_label = Label(window, bg="SlateBlue2", fg="white", text= "Are you ready to take your typing skills to the next level? \n\nDive into the world of speed and precision with the Typing Speed Test app \nWhere every keystroke counts and improvement is just a tap away!", font="helvetica 16 bold", pady=20, padx=20)
intro_label.grid(column=1, row=0, columnspan=4)

# Generate random words
generate_button = Button(window, borderwidth=0, highlightthickness=0, text="Generate", command=generate_words)
generate_button.configure(width=20, height=2, bg="gray14", fg="white", font="helvetica 14")
generate_button.grid(column=2, row=1, pady=40)

# Show user input field and start counting time
start_button = Button(window, borderwidth=0, highlightthickness=0, text="Start", command=start_typing)
start_button.configure(width=20, height=2, bg="gray14", fg="white", font="helvetica 14")
start_button.grid(column=3, row=1, pady=40)

window.mainloop()