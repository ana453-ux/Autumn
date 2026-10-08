import tkinter as tk
import random
import math

root = tk.Tk()
root.title("Feuilles d'automne qui tombent")
root.geometry("800x600")
root.resizable(width=True, height=True)

canvas = tk.Canvas(root, width=800, height=600, background="black")
canvas.pack()

colors = [
    "#ff7043",
    "#ff9800",
    "#fdd835",
    "#e53935",
    "#8d6e63",
]

# Chaque feuille : [x, y, taille, vitesse, phase, oscillation, couleur]
leaves = []
for _ in range(90):
    leaves.append([
        random.randint(0, 800),
        random.randint(-600, 600),
        random.randint(5, 11),
        random.uniform(1.5, 4),
        random.uniform(0, 6.28),
        random.uniform(0.02, 0.06),
        random.choice(colors),
    ])


def animate():
    canvas.delete("all")

    # Arrière-plan
    canvas.create_rectangle(0, 0, 800, 600, fill="#183047", outline="")

    # Sol
    canvas.create_rectangle(0, 540, 800, 600, fill="#4e342e", outline="")

    # Arbres
    for tx in [100, 700]:
        # Tronc
        canvas.create_rectangle(tx - 14, 300, tx + 14, 560,
                                fill="#5d4037", outline="")
        # Feuillage
        canvas.create_oval(tx - 90, 150, tx + 90, 330,
                           fill="#9e3d20", outline="")
        canvas.create_oval(tx - 110, 190, tx + 50, 350,
                           fill="#c75b25", outline="")

    # Feuilles
    for leaf in leaves:
        # D'abord la mise à jour
        leaf[1] += leaf[3]                  # chute selon la vitesse
        leaf[4] += leaf[5]                  # avance la phase
        leaf[0] += math.sin(leaf[4]) * 2.5  # balancement latéral

        if leaf[1] > 610:                   # réapparition en haut
            leaf[0] = random.randint(0, 800)
            leaf[1] = random.randint(-100, 0)
            leaf[2] = random.randint(5, 11)

        # Ensuite on déballe les valeurs et on dessine
        x, y, size, speed, phase, wave, color = leaf

        canvas.create_oval(
            x - size, y - size * 0.55,
            x + size, y + size * 0.55,
            fill=color,
            outline=""
        )
        canvas.create_line(
            x - size, y,
            x + size, y,
            fill="#6d2c1b",
            width=1
        )

    root.after(30, animate)  # ~33 images/seconde


animate()
root.mainloop()