class Carte:
    """ Classe représentant une carte"""

    def __init__(self, couleur, hauteur):
        if couleur not in {"coeur", "trèfle", "carreau", "pique"}:
            raise ValueError("Les cartes ne peuvent qu'être de typte coeur, trèfle, carreau ou pique")
        else:
            self.couleur = couleur
        if hauteur not in {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "V", "D", "R"}:
            raise ValueError("Les cartes ne peuvent qu'être de valeur 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, V, D, R")
        else:
            self.hauteur = hauteur

    def __str__(self):
        forme_couleur = {"coeur": "\u2665", "trèfle": "\u2663", "carreau": "\u2666", "pique": "\u2660"}
        return f"{self.hauteur}{forme_couleur[self.couleur]}"

