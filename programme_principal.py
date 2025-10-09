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
from random import randrange

"""
Pseudocode :
importer random 

Carte bingo du joueur = fonction qui génère une carte unique pour le joueur 

Boucle while :
    Combinaison lettre-chiffre = combinaison random choisie à partir de la liste de combinaisons (ex: B-12, I-18, ...)
    Afficher la carte BINGO du joueur
    Afficher la combinaison lettre-chiffre pigée
    
    Utiliser la fonction placer_jeton(combinaison_pigee: str, carte_joueur: list[list[str and int]]) -> list[list[str and int]]:
        Demander au joueur de placer son jeton au bon endroit (choisir la bonne colonne et la bonne ligne)
        Si la combinaison n'existe pas dans la carte du joueur, le joueur doit répondre avec 'x' (ou autre symbole)
        Si le joueur ne choisit pas la bonne réponse, on lance un message d'erreur 
        Si le joueur choisit le bon endroit, on remplace le chiffre assigné à cette case par un jeton 
        (o, *, peu importe)
        Return la carte bingo du joueur avec son nouveau jeton (ou inchangée si la combinaison n'existe pas 
        dans la carte du joueur) 
    
    Utiliser la fonction bingo_gagnant(carte_joueur: list[list[str and int]]) -> str:
        Pour chaque colonne de la liste carte_joueur:
            Si indexe y == str, 
                return "bingo gangnant"
        Pour chaque ligne de la liste carte_joueur:
            Si indexe y == str, 
                return "bingo gangnant"
        Pour chaque ligne diagonale dans la liste carte_joueur:
            Si indexe y == str, 
                return "bingo gangnant"
    ^^^^^^^^ à terminer plus tard
    
    if bingo = "bingo gangnant":
        break    
    
    
    
  
"""

from module import *
import random

if __name__ == '__main__':
    liste_combinaisons = creer_liste_combinaisons()
    carte_joueur = generer_carte(liste_combinaisons)

    while True:
        combinaison_pigee = random.choice(liste_combinaisons)
        for ligne in carte_joueur:
            print(ligne)
        print(combinaison_pigee)

        placer_jeton() #TODO: créer fonction
        bingo = bingo_gagnant() #TODO: créer fonction

        if bingo == "BINGO gagnant!":
            break





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
    x = True

    # print pour afficher la grille
    grille = [

        ["B", "I","N","G","O" ],
        [],
        [],
        [],
        [],
        [],
    ]
    #remplacer cases par "x"
    jeton = input("Place le jeton à la case nommer", )

    #ligne gagnante

    while True:
        if x * 5  in liste_combinaisons:
            print("BINGO gagnant!")
        elif randrange(0 , 60) == 0:
            input(random.choice(grille))
        elif random.choice(grille) in carte_joueur:
            input(x) in grille
            print("Pas encore de BINGO.")
        else :
            print(x in combinaison_pigee)

        break


bingo_gagnant(carte_joueur, combinaison_pigee, jeton)


#Fonction placer le jeton
####




































