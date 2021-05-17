class Carte:
    """ Classe représentant une carte"""

    def __init__(self, couleur, hauteur):
        if couleur not in {"coeur", "trèfle", "carreau", "pique"}:
            raise ValueError("Les cartes ne peuvent qu'être de type coeur, trèfle, carreau ou pique")
        else:
            self.couleur = couleur
        if hauteur not in {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "V", "D", "R"}:
            raise ValueError("Les cartes ne peuvent qu'être de valeur 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, V, D, R")
        else:
            self.hauteur = hauteur

    def __str__(self):
        forme_couleur = {"coeur": "\u2665", "trèfle": "\u2663", "carreau": "\u2666", "pique": "\u2660"}
        return f"{self.hauteur}{forme_couleur[self.couleur]}"

    def valeur(self):
        if isinstance(self.hauteur, str):
            if self.hauteur == "V":
                return 11
            elif self.hauteur == "D":
                return 12
            else:
                return 13
        elif self.hauteur == 1:
            return 14
        else:
            return self.hauteur

    def __eq__(self, other):
        """ carte self égale à carte other"""
        if self.valeur() == other.valeur():
            return True
        else:
            return False

    def __lt__(self, other):
        """carte strictement inférieure à other"""
        if self.valeur() < other.valeur():
            return True
        else:
            return False

    def __gt__(self, other):
        """Strictement inférieur"""
        if self.valeur() > other.valeur():
            return True
        else:
            return False

carte = Carte("coeur", "D")
carte2 = Carte("coeur", "R")
print(carte)
print(carte == carte2)