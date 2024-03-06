import tkinter as tk
from PIL import Image, ImageTk  # Dodano import modułu Image z PIL
import random

def resize_window(event):
    width = event.width
    height = event.height
    root.geometry(f"{width}x{height}")

def button_click():
    words = ["Odnajdź STO", "Ostry na Cienkim dla pan doktor", "pójdź do papieża", "Idź do telewizora", "Upoluj Bobra", "Zrób Lekcje na Duolingo", "Zrób Workout", "Odnajdź unikalny śmieć", "bizoj", "zagraj w flappy gremlin"]
    random_word = random.choice(words)
    label.config(text=random_word)

root = tk.Tk()
root.title("Questy na Spotkania")


# Dodawanie tła
bg_image = Image.open("tapeta.png")
bg_photo = ImageTk.PhotoImage(bg_image)
bg_label = tk.Label(root, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)







# Rozmiar początkowy okna
initial_width = 400
initial_height = 600
root.geometry(f"{initial_width}x{initial_height}")

# Ustawienie minimalnego rozmiaru okna
root.minsize(400, 600)

# Ustawienie dostosowania rozmiaru okna
root.bind("<Configure>", resize_window)

# Przycisk
button = tk.Button(root, text="Losuj Quest", command=button_click)
button.pack(pady=20)

# Etykieta do wyświetlenia losowanego słowa
label = tk.Label(root, text="", font=("Helvetica", 18))
label.pack()

# Pętla główna programu
root.mainloop()