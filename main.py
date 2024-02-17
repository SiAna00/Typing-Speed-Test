from tkinter import *
import random
from text import words

# Create GUI with Tkinter
window = Tk()
window.title("Typing Speed Test")
window.geometry("500x500")
window.configure(bg="Purple")

# Generate random words
random_words = random.choice(words, k=50)
words_label = Label(text=random_words)
words_label.pack()

# Count time (1 minute)

# Count how many words per minute

window.mainloop()