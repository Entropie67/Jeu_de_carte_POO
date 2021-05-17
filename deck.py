from carte import Carte
from random import shuffle


class Deck:
    """Classe modélisant un paquet de carte"""

    def __init__(self):
        self.cartes = []
        self._build()

    def _build(self):
        """permet de remplir le paquet avec des cartes dans l'ordre"""
        self.cartes = [Carte(c, h) for c in ["coeur", "trèfle", "carreau", "pique"]
                    for h in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "V", "D", "R"]]

    def __str__(self):
        return " - ".join(list(map(str, self.cartes)))

    def __len__(self):
        return len(self.cartes)

    def melange(self):
        """ Méthode pour mélanger un paquet"""
        shuffle(self.cartes)

    def donne_carte(self, n):
        """Donne les n cartes du haut du paquet"""
        return [self.cartes.pop() for _ in range(n)]

