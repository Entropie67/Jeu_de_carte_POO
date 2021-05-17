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

    def start(self):
        paquet = Deck()
        paquet.melange()
        nb_carte = len(paquet)//2
        for joueur in self.liste_joueurs:
            joueur.donne_main(paquet, nb_carte)
            print(joueur)
        self._bataille()

    def _bataille(self):

        carte_1 = self.liste_joueurs[0].main[1]
        carte_2 = self.liste_joueurs[1].main[1]
        print(f"{self.liste_joueurs[0].nom} pose la carte {carte_1}")
        self.liste_joueurs[0].pose_carte(self.liste_joueurs[0].main[1])
        print(f"{self.liste_joueurs[1].nom} pose la carte {carte_2}")
        self.liste_joueurs[1].pose_carte(self.liste_joueurs[1].main[1])

        print(f"{carte_1} VS {carte_2}")




partie = Bataille(2)
print(partie)
partie.start()

