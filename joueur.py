from deck import Deck

class Joueur:

    def __init__(self, nom):
        self.nom = nom
        self.main = []

    def __str__(self):
        main = " - ".join(list(map(str, self.main)))
        return f"Le joueur : {self.nom} \n possède les cartes : {main}"

    def donne_main(self, deck):
        self.main = deck.donne_carte(5)




jeu = Deck()
joueur = Joueur("Albert")
print(joueur)
jeu.melange()
joueur.donne_main(jeu)
print(joueur)