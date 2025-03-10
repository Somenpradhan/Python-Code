import tkinter as tk
from tkinter import messagebox
import random

# List of words for the game
WORD_LIST = ["python", "computer", "science", "programming", "developer", "keyboard", "software", "machine", "learning", "intelligence"]

def shuffle_word(word):
    word = list(word)
    random.shuffle(word)
    return ''.join(word)

def check_word():
    user_input = entry.get().strip().lower()
    if user_input == current_word:
        score.set(score.get() + 1)
        messagebox.showinfo("Correct!", "Well done! You guessed the word.")
        next_word()
    else:
        messagebox.showerror("Incorrect!", "Oops! Try again.")

def next_word():
    global current_word, scrambled_word
    current_word = random.choice(WORD_LIST)
    scrambled_word = shuffle_word(current_word)
    label_word.config(text=f"Scrambled word: {scrambled_word}")
    entry.delete(0, tk.END)

def quit_game():
    root.destroy()

def reset_game():
    score.set(0)
    next_word()

# Initialize the main window
root = tk.Tk()
root.title("Word Game")
root.geometry("600x400")
root.resizable(False, False)
root.config(bg="#cce7ff")  # Light blue background

# Variables to store the current word, scrambled word, and score
current_word = ""
scrambled_word = ""
score = tk.IntVar(value=0)

# Heading
label_heading = tk.Label(root, text="Word Game", font=("Helvetica", 28, "bold"), bg="#cce7ff", fg="#003366")
label_heading.pack(pady=20)

# Score label
frame_score = tk.Frame(root, bg="#cce7ff")
frame_score.pack(anchor="ne", padx=10, pady=5)
label_score_title = tk.Label(frame_score, text="Score:", font=("Helvetica", 16), bg="#cce7ff", fg="#003366")
label_score_title.pack(side="left")
label_score = tk.Label(frame_score, textvariable=score, font=("Helvetica", 16), bg="#cce7ff", fg="#003366")
label_score.pack(side="left")

# Scrambled word label
label_word = tk.Label(root, text="", font=("Helvetica", 20, "italic"), bg="#cce7ff", fg="#002244")
label_word.pack(pady=20)

# Entry box
entry = tk.Entry(root, font=("Helvetica", 16), justify="center", bd=2, relief="solid")
entry.pack(pady=20, ipadx=10, ipady=5)

# Buttons Frame
frame_buttons = tk.Frame(root, bg="#cce7ff")
frame_buttons.pack(pady=10)

# Check button
button_check = tk.Button(frame_buttons, text="Check", font=("Helvetica", 14), bg="#4caf50", fg="white", command=check_word, width=12)
button_check.grid(row=0, column=0, padx=5, pady=5)

# Next word button
button_next = tk.Button(frame_buttons, text="Next Word", font=("Helvetica", 14), bg="#2196f3", fg="white", command=next_word, width=12)
button_next.grid(row=0, column=1, padx=5, pady=5)

# Reset button
button_reset = tk.Button(frame_buttons, text="Reset Game", font=("Helvetica", 14), bg="#ff9800", fg="white", command=reset_game, width=12)
button_reset.grid(row=0, column=2, padx=5, pady=5)

# Quit button
button_quit = tk.Button(frame_buttons, text="Quit", font=("Helvetica", 14), bg="#f44336", fg="white", command=quit_game, width=12)
button_quit.grid(row=0, column=3, padx=5, pady=5)

# Start the game with the first word
next_word()

# Run the application
root.mainloop()
