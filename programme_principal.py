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
"""
Pseudocode :

##Fonctions:
creer_liste_combinaisons() -> list:
    Fonction qui crée une liste avec toutes les combinaisons lettres-chiffres possibles à piger dans un
    jeu de BINGO.
    :return: liste des combinaisons
    ----------------------------------
    Liste lettres = ["B", "I", "N", "G", "O"]
    Liste combinaisons = [] 
    
    Chiffre = 0
    Index de la liste lettre = 0
    Boucle for (pour chaque lettre dans liste lettres):
        Lettre = liste lettres(index de la liste lettre)
        Boucle for (15 fois):
            Chiffre +=1 (le chiffre 0 n'est pas inclu dans ce jeu de bingo)
            Ajouter lettre + chiffre à la liste de combinaisons
        Index de la liste lettre +=1
    Return liste combinaisons
 
generer_carte(liste: list) -> list:
    Fonction qui génère une carte BINGO aléatoire pour le joueur
    :param liste: liste de combinaisons
    :return: une liste représentant la carte du joueur
    --------------------------------------------------
    Carte joueur (vide) = [["B", "I", "N", "G", "O" ], [], [], [], [], []]
    
    Avec une boucle for, creer une liste contenant tous les chiffres possibles dans un jeu de BINGO.
    
    Avec des split, séparer la liste de chiffres en sections selon leur lettre correspondante.
    (B(1-15), I(16-30), N(31-45), G(46-60), O(61-75)) Note: quand on fait un split, le premier chiffre n'est pas inclus.
    Liste chiffres = liste 2D contenant chaque section de chiffres par lettre
    
    Choisir les chiffres aléatoirement et les ajouter dans la liste carte joueur
    Boucle for i in range(pour chaque lettre):
        Boucle for j in range(pour chaque lettre): 
            choix chiffre = random.choice(liste chiffres[j])
            Ajouter chiffre à la carte joueur[i+1]
            Retirer chiffre de la liste chiffres
    
    Changer la case du milieu pour un espace libre
    Return la carte joueur
            

placer_jeton(combi_pigee: str, carte: list[list[str and int]]) -> list[list[str and int]]:
    Fonction place un jeton sur la carte BINGO
    :param combi_pigee: la combinaison lettre-chiffre pigée
    :param carte: la carte BINGO du joueur
    :return: la carte bingo du joueur avec modification (jeton)
    ---------------------------------------
    Demander au joueur de placer son jeton au bon endroit (choisir la bonne colonne et la bonne ligne)
    Si combi_pigee n'existe pas dans la carte du joueur, le joueur doit répondre avec 'x' (ou autre symbole)
    Si le joueur ne choisit pas la bonne réponse, on lance un message d'erreur 
    Si le joueur choisit le bon endroit, on remplace le chiffre assigné à cette case par un jeton 
    (o, *, peu importe tant que ce n'est pas un chiffre)
    Return la carte bingo du joueur avec son nouveau jeton (ou inchangée si la combinaison n'existe pas 
    dans la carte du joueur) 

bingo_gagnant(c_joueur: list[list[str and int]]) -> str:
    Fonction qui détermine si on a une ligne BINGO gagnante
    :param c_joueur: la carte BINGO du joueur
    :return: "BINGO gagnant!" ou "Pas encore de BINGO."
    ------------------------------------------
    gagné = False
    Pour chaque colonne de la liste c_joueur:
        Si les indexes de la colonne sont tous des string, 
            gagné = True
    Pour chaque ligne de la liste c_joueur:
        Si les indexes de la ligne sont tous des string, 
            gagné = True
    Pour chaque ligne diagonale dans la liste c_joueur:
        Si les indexes de la ligne diagonale sont tous des string, 
            gagné = True
    
    Si gagné == True:
        return "BINGO gagnant!"
    Sinon:
        return "Pas encore de BINGO."

##Code Principal: 
importer random 

Liste combinaisons = fonction creer_liste_combinaisons()
Carte bingo du joueur = fonction generer_carte(liste combinaisons)
    
Boucle while :
    Combinaison lettre-chiffre = random.choice(liste combinaisons)
    Retirer la combinaison de la liste de combinaisons
    Afficher la carte BINGO du joueur
    Afficher la combinaison lettre-chiffre pigée
    
    Utiliser la fonction placer_jeton(combinaison_pigee, carte_joueur)
    
    Utiliser la fonction bingo_gagnant(carte_joueur)
    
    if bingo == "BINGO gagnant!":
        break 
"""
from random import randrange

from module import *
import random

if __name__ == '__main__':
    liste_combinaisons = creer_liste_combinaisons()
    carte_joueur = generer_carte(liste_combinaisons)

    while True:
        combinaison_pigee = random.choice(liste_combinaisons)
        liste_combinaisons.remove(combinaison_pigee)

        for ligne in carte_joueur:
            print(ligne)
        print(combinaison_pigee)

        placer_jeton(combinaison_pigee, carte_joueur)
        bingo = bingo_gagnant(carte_joueur) #TODO: créer fonction

        if bingo == "BINGO gagnant!":
            break