import tkinter
import random

# ---------------------------- Game Logic ------------------------------- #
def reset_game():
    """Resets the game by generating a new random number and clearing inputs."""
    global target_number, attempts
    target_number = random.randint(1, 100)
    attempts = 0
    guess_entry.delete(0, tkinter.END)
    result_label.config(text="Guess a number!", fg="black")
    check_button.config(state="normal")

def check_guess():
    """Checks if the guessed number is too low, too high, or correct."""
    global attempts
    guess = guess_entry.get()

    if not guess.isdigit():
        result_label.config(text="Enter a valid number!", fg="red")
        return

    guess = int(guess)
    attempts += 1

    if guess < target_number:
        result_label.config(text="Too Low!", fg="red")
    elif guess > target_number:
        result_label.config(text="Too High!", fg="red")
    else:
        result_label.config(text=f"Correct! 🎉 (Attempts: {attempts})", fg="green")
        check_button.config(state="disabled")  # Disable check button after winning

# ---------------------------- UI Setup ------------------------------- #
screen = tkinter.Tk()
screen.title("Number Guessing Game")
screen.config(padx=50, pady=50)

# Title Label
tkinter.Label(screen, text="🔢 Number Guessing Game 🔢", font=("Arial", 20, "bold")).grid(row=0, column=0, columnspan=2, pady=10)

# Input Field
tkinter.Label(screen, text="Enter a number (1-100):", font=("Arial", 14)).grid(row=1, column=0, padx=10, pady=5)
guess_entry = tkinter.Entry(screen, width=10, font=("Arial", 14))
guess_entry.grid(row=1, column=1)

# Result Label
result_label = tkinter.Label(screen, text="Guess a number!", font=("Arial", 16))
result_label.grid(row=2, column=0, columnspan=2, pady=10)

# Buttons
check_button = tkinter.Button(screen, text="Check", command=check_guess, font=("Arial", 14), width=10)
check_button.grid(row=3, column=0, pady=5)

reset_button = tkinter.Button(screen, text="Restart", command=reset_game, font=("Arial", 14), width=10)
reset_button.grid(row=3, column=1, pady=5)

# Initialize the game
reset_game()

screen.mainloop()
