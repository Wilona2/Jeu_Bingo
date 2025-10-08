"""
Données d’entrée :
Espace sur la carte BINGO où on place un jeton

Données de sortie :
Liste 2D qui représente la carte BINGO du joueur
Liste des combinaisons lettre-nombre possibles dans un jeu (ex: B-2, O-65, ...)
Combinaison lettre-nombre pigée aléatoirement

Fonctions :
Wilo
Fonction qui génère une carte BINGO aléatoire pour le joueur
Fonction qui crée une liste avec toutes les combinaisons lettres-chiffres possibles à piger dans un jeu de BINGO.

Maryam
Fonction qui détermine si on a une ligne BINGO gagnante
Fonction qui place un jeton sur la carte BINGO

"""
from module import *
#Données d'entrée

#Données de sortie
liste_combinaisons = creer_liste_combinaisons()
carte_joueur = generer_carte(liste_combinaisons)

combinaison_pigee = random.choice(liste_combinaisons)










#Fonction qui détermine si on a une ligne BINGO gagnante
def bingo_gagnant(grille, B: int,I: int,N: int,G :int,O: int, jeton :int ) -> None:
    """
    Fonction qui détermine si on a une ligne BINGO gagnante
    :param grille: grille de BINGO
    :param B: colonne de grille
    :param I: colonne de grille
    :param N: colonne de grille
    :param G: colonne de grille
    :param O: colonne de grille
    :param jeton: le jeton , x , placer sur la grille BINGO,
    :return: ???
    """
# print pour afficher la grille
grille = [

    ["B", "I","N","G","O" ],
    ["14", "18","40","52","65"],
    ["6", "27", "45","59","66"],
    ["5", "17", "*","50", "73"],
    ["9","25", "31","57", "62"],
    ["4","21", "39","48", "67"],
]
#remplacer cases par "x"
jeton = input("Place le jeton à la case nommer", )

#ligne gagnante
import random
if bingo_gagnant(grille):
    for ligne in grille:
        print(ligne)
elif bingo_gagnant(grille, jeton):
    for colonne in grille:
        print(colonne)
else :
    print(grille)

if bingo_gagnant(carte_joueur):
    print("BINGO gagnant !")
else :
    print("Pas encore de BINGO.")


if random.random():






































