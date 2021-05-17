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
        self._bataille()

    def _bataille(self):
        compteur = 0
        joueur1 = self.liste_joueurs[0]
        joueur2 = self.liste_joueurs[1]
        print(joueur1)
        print(joueur2)
        while len(joueur1.main) > 0 and len(joueur2.main) > 0:
            compteur += 1
            pile = []
            gagnant, pli = self.pli(pile)
            gagnant.ramasse_carte(pli)

        print("\n *** La partie est terminée *** \n")
        if len(joueur2.main) > len(joueur2.main):
            print(f"{joueur2.nom} gagne en {compteur} tours !")
        else:
            print(f"{joueur1.nom} gagne en {compteur} tours !")


    def pli(self, pile):
        joueur1 = self.liste_joueurs[0]
        joueur2 = self.liste_joueurs[1]
        carte_1 = joueur1.main[0]
        carte_2 = joueur2.main[0]
        pile.append(carte_1)
        pile.append(carte_2)
        print(joueur1)
        print(joueur2)
        print(f"{self.liste_joueurs[0].nom} pose la carte {carte_1}")
        self.liste_joueurs[0].pose_carte(self.liste_joueurs[0].main[0])
        print(f"{self.liste_joueurs[1].nom} pose la carte {carte_2}")
        self.liste_joueurs[1].pose_carte(self.liste_joueurs[1].main[0])
        print(f"{carte_1} VS {carte_2}")
        if carte_1 > carte_2:
            print(f"{carte_1} est plus forte, c'est {joueur1.nom} qui gagne le pli")
            gagnant = joueur1
        elif carte_1 == carte_2:
            print("égalité")
            self.pli(pile)
            gagnant = joueur1
        else:
            print(f"{carte_2} est plus forte, c'est {joueur2.nom} qui gagne le pli")
            gagnant = joueur2
        return gagnant, pile


partie = Bataille(2)
print(partie)
partie.start()

