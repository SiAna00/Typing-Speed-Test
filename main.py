from tkinter import *
import random
import time
from text import words

def generate_words():
    random_words = random.choices(words, k=50)
    words_label = Label(window, bg="bisque", fg="gray18", text=random_words, font="helvetica 18", wraplength=740, pady=20, padx=20)
    words_label.grid(column=0, row=2, columnspan=4, pady=40)
    

def count_wpm():
    user_input = input_field.get("1.0", END)
    user_words = user_input.split()

    # Count how many words per minute
    wpm = len(user_words)
    intro_label.config(text=f"Your typing speed is {wpm} WPM.", fg="gray13", font="helvetica 20 bold")


def start_typing():
    global input_field

    # Create user input field
    input_field = Text(window, borderwidth=0, highlightthickness=0, bg="bisque", fg="gray18", font="helvetica 18", width=60, height=10, pady=20, padx=20)
    input_field.grid(column=0, row=4, columnspan=4, padx=20, pady=20)

    # Count time (1 minute)
    window.after(60000, count_wpm)


# Create GUI with Tkinter
window = Tk()
window.title("Typing Speed Test")
window.configure(bg="SlateBlue2", padx=100, pady=100)

image = PhotoImage(file="typing_machine.png")
image_label = Label(window, image=image)
image_label.grid(column=2, row=0, columnspan=2, rowspan=2, pady=20, padx=20)

intro_label = Label(window, bg="SlateBlue2", wraplength=440, justify="left", fg="white", text= "Are you ready to take your typing skills to the next level? \n\nDive into the world of speed and precision with the Typing Speed Test app", font="helvetica 16 bold", pady=20, padx=20)
intro_label.grid(column=0, row=0, columnspan=2)

# Generate random words
generate_button = Button(window, borderwidth=0, highlightthickness=0, text="Generate", command=generate_words)
generate_button.configure(width=15, height=2, bg="gray14", fg="white", font="helvetica 14")
generate_button.grid(column=0, row=1, pady=40)

# Show user input field and start counting time
start_button = Button(window, borderwidth=0, highlightthickness=0, text="Start", command=start_typing)
start_button.configure(width=15, height=2, bg="gray14", fg="white", font="helvetica 14")
start_button.grid(column=1, row=1, pady=40)

window.mainloop()