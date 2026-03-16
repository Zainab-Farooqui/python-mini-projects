# Python Tkinter GUI based "LOVE CALCULATOR"

from tkinter import *
import random

root = Tk()
root.geometry("420x320")
root.title("💖 Love Calculator 💖")
root.configure(bg="#ffccd5")


def calculate_love():
    value = random.randint(1, 100)

    if value > 60:
        # Lovey dovey UI
        root.configure(bg="#ffb3c6")
        result.config(
            text=f"💘 Love Percentage: {value}% 💘\nPerfect Couple! 💞",
            fg="darkred",
            bg="#ffb3c6"
        )
        heading.config(bg="#ffb3c6")

    else:
        # Sad UI
        root.configure(bg="#d9d9d9")
        result.config(
            text=f"💔 Love Percentage: {value}% 💔\nMaybe just friends 😢",
            fg="black",
            bg="#d9d9d9"
        )
        heading.config(bg="#d9d9d9")


heading = Label(
    root,
    text="💖 LOVE CALCULATOR 💖",
    font=("Comic Sans MS", 18, "bold"),
    bg="#ffccd5",
    fg="#b30059"
)
heading.pack(pady=10)

subheading = Label(
    root,
    text="Check how much you love each other 💞",
    font=("Arial", 11),
    bg="#ffccd5"
)
subheading.pack(pady=5)


slot1 = Label(root, text="Enter Your Name", font=("Arial", 11, "bold"), bg="#ffccd5")
slot1.pack()

name1 = Entry(root, font=("Arial", 11), width=25, bd=3)
name1.pack(pady=5)


slot2 = Label(root, text="Enter Your Partner Name", font=("Arial", 11, "bold"), bg="#ffccd5")
slot2.pack()

name2 = Entry(root, font=("Arial", 11), width=25, bd=3)
name2.pack(pady=5)


bt = Button(
    root,
    text="💗 Calculate Love 💗",
    font=("Arial", 11, "bold"),
    bg="#ff4d6d",
    fg="white",
    width=18,
    command=calculate_love
)
bt.pack(pady=15)


result = Label(
    root,
    text="Love Percentage will appear here",
    font=("Arial", 13, "bold"),
    bg="#ffccd5",
    fg="#660033"
)
result.pack(pady=10)


root.mainloop()