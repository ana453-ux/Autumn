# 🍂 Feuilles d'automne qui tombent

Une petite animation en Python qui montre des feuilles d'automne tombant doucement devant deux arbres, sur un fond de ciel crépusculaire.

## Aperçu

- 90 feuilles de tailles, de vitesses et de couleurs différentes (orange, jaune, rouge, brun)
- Balancement latéral réaliste pendant la chute
- Les feuilles réapparaissent en haut une fois arrivées en bas
- Décor simple : ciel bleu nuit, sol brun et deux arbres au feuillage roux

## Prérequis

- Python 3
- Tkinter (inclus avec la plupart des installations de Python)

Aucune bibliothèque externe n'est nécessaire.

> Sous Linux, si Tkinter est absent : `sudo apt install python3-tk`

## Lancement

```bash
python Autumn.py
```

Une fenêtre de 800 × 600 pixels s'ouvre et l'animation démarre automatiquement. Fermez la fenêtre pour quitter.

## Personnalisation

Quelques réglages faciles à modifier dans `Autumn.py` :

| Ce que vous voulez changer | Où |
|---|---|
| Le nombre de feuilles | `range(90)` dans la création de la liste `leaves` |
| Les couleurs des feuilles | la liste `colors` |
| La vitesse de chute | `random.uniform(1.5, 4)` |
| L'amplitude du balancement | le facteur `2.5` dans `math.sin(leaf[4]) * 2.5` |
| La fluidité de l'animation | `root.after(30, animate)` (valeur en millisecondes) |
| La position des arbres | la liste `[100, 700]` dans la boucle des arbres |

## Fonctionnement

Chaque feuille est stockée sous la forme d'une liste :

```
[x, y, taille, vitesse, phase, oscillation, couleur]
```

À chaque image (environ toutes les 30 ms), le programme efface le canvas, redessine le décor, met à jour la position de chaque feuille puis la dessine sous forme d'ovale avec une nervure centrale.

## Licence

Libre d'utilisation et de modification.
