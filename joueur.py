from deck import Deck

class Joueur:

    def __init__(self, nom):
        self.nom = nom
        self.main = []

    def __str__(self):
        main = " - ".join(list(map(str, self.main)))
        return f"Le joueur : {self.nom} \n possède les cartes : {main}"

    def donne_main(self, deck, n):
        self.main = deck.donne_carte(n)

    def pose_carte(self, carte):
        self.main.remove(carte)

    def ramasse_carte(self, liste_cartes):
        self.main.extend(liste_cartes)


