import tkinter as tk
import random

# Hangman stages
hangman_stages = [
    """\n     -----\n     |   |\n         |\n         |\n         |\n         |\n    =====\n    """,
    """\n     -----\n     |   |\n     O   |\n         |\n         |\n         |\n    =====\n    """,
    """\n     -----\n     |   |\n     O   |\n     |   |\n         |\n         |\n    =====\n    """,
    """\n     -----\n     |   |\n     O   |\n    /|   |\n         |\n         |\n    =====\n    """,
    """\n     -----\n     |   |\n     O   |\n    /|\\  |\n         |\n         |\n    =====\n    """,
    """\n     -----\n     |   |\n     O   |\n    /|\\  |\n    /    |\n         |\n    =====\n    """,
    """\n     -----\n     |   |\n     O   |\n    /|\\  |\n    / \\  |\n         |\n    =====\n    """
]

# List of words
animals = [
    "aardvark", "alligator", "alpaca", "antelope", "ape", "armadillo", "baboon", "badger", "bat", "bear",
    "beaver", "bison", "boar", "buffalo", "butterfly", "camel", "caribou", "cat", "caterpillar"
]

def reset_game():
    global word, placeholder, lifes, guessed_letters
    word = random.choice(animals)
    placeholder = ['_' for _ in word]
    lifes = 6
    guessed_letters = set()
    result_label.config(text="", fg="black")
    update_display()

def update_display():
    word_label.config(text=' '.join(placeholder))
    hangman_label.config(text=hangman_stages[6 - lifes])
    lives_label.config(text=f"Lives Remaining: {lifes}")

def guess_letter(letter):
    global lifes
    if letter in guessed_letters:
        return
    guessed_letters.add(letter)
    if letter in word:
        for i, char in enumerate(word):
            if char == letter:
                placeholder[i] = letter
    else:
        lifes -= 1
    update_display()
    check_game_status()

def check_game_status():
    if '_' not in placeholder:
        result_label.config(text="You Win!", fg="green")
        play_again_button.pack()
    elif lifes == 0:
        result_label.config(text=f"You Lost! The word was {word}", fg="red")
        play_again_button.pack()

# Set up UI
root = tk.Tk()
root.title("Hangman Game")
root.geometry("400x500")
root.config(bg="white")

hangman_label = tk.Label(root, text=hangman_stages[0], font=("Courier", 12), bg="white")
hangman_label.pack()

word_label = tk.Label(root, text=' '.join(['_' for _ in animals[0]]), font=("Arial", 20), bg="white")
word_label.pack()

lives_label = tk.Label(root, text=f"Lives Remaining: 6", font=("Arial", 14), bg="white")
lives_label.pack()

buttons_frame = tk.Frame(root, bg="white")
buttons_frame.pack()
for letter in "abcdefghijklmnopqrstuvwxyz":
    tk.Button(buttons_frame, text=letter, font=("Arial", 12), width=3, command=lambda l=letter: guess_letter(l)).pack(side=tk.LEFT)

result_label = tk.Label(root, text="", font=("Arial", 14), bg="white")
result_label.pack()

play_again_button = tk.Button(root, text="Play Again", font=("Arial", 14), command=reset_game)
play_again_button.pack()
play_again_button.pack_forget()

reset_game()
root.mainloop()
