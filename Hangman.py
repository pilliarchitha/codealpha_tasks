import tkinter as tk
import random

# words to guess 
words = ["apple", "mango", "banana", "orange", "grapes"]

# pick one
word = random.choice(words)
guessed = []
wrong = 0
max_wrong = 6

# showing words with blanks
def show_word():
    s = ""
    for ch in word:
        if ch in guessed:
            s += ch + " "
        else:
            s += "_ "
    lbl_word.config(text=s)

    # check win
    if "_" not in s:
        lbl_result.config(text="You Won!!! 🎉🎉🎉")

#  guessing part
def do_guess():
    global wrong
    letter = txt_guess.get().lower()
    txt_guess.delete(0, tk.END)

    if letter in word:
        if letter not in guessed:  # avoid duplicates
            guessed.append(letter)
        lbl_result.config(text="Good one :)")
    else:
        wrong += 1
        lbl_result.config(text="Nope... tries left: " + str(max_wrong - wrong))

    show_word()

    if wrong >= max_wrong:
        lbl_result.config(text="Game Over :( word was " + word)

# window setup
win = tk.Tk()
win.title("Hangman")
win.geometry("350x250")

lbl_title = tk.Label(win, text="Hangman Game", font=("Arial", 16))
lbl_title.pack(pady=10)

lbl_word = tk.Label(win, text="", font=("Arial", 18))
lbl_word.pack(pady=10)

txt_guess = tk.Entry(win)
txt_guess.pack(pady=5)

btn = tk.Button(win, text="Guess", command=do_guess)
btn.pack(pady=5)

lbl_result = tk.Label(win, text="")
lbl_result.pack(pady=10)

show_word()

# run it
win.mainloop()
