from deck import Deck
from joueur import Joueur
class Bataille:
    """classe modélisant une partie de bataille fermée"""

    def __init__(self, nb_joueurs):

        self.deck = Deck()
        self.nb_joueurs = nb_joueurs
        self.liste_joueurs = self._players()

    def _players(self):

        joueurs = []
        for i in range(self.nb_joueurs):
            nom = input(f"Veuillez rentrer le nom de joueur {i+1} : \n")
            joueurs.append(Joueur(nom))
        return joueurs

    def __str__(self):
        r = " - ".join([j.nom for j in self.liste_joueurs])
        return f" Partie de bataille fermée opposant les joureurs : \n {r}"

partie = Bataille(2)
print(partie)