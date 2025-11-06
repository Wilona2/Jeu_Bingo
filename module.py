import random
#Wilo
def creer_liste_combinaisons() -> list[str]:
    """
    Fonction qui crée une liste avec toutes les combinaisons lettres-chiffres possibles à piger dans un
    jeu de BINGO.
    :return: liste des combinaisons
    """
    liste_combinaisons = []
    liste_lettres = ["B", "I", "N", "G", "O"]
    nombre = 0
    index = 0
    for i in range(len(liste_lettres)):
        lettre = liste_lettres[index]
        for j in range(15):
            nombre += 1
            liste_combinaisons.append(f"{lettre}-{nombre}")
        index += 1
    return liste_combinaisons
def generer_carte(liste: list[str]) -> list[list]:
    """
    Fonction qui génère une carte BINGO aléatoire pour le joueur
    :param liste: liste de combinaisons
    :return: une liste représentant la carte du joueur
    """
    carte_joueur = [["B", "I", "N", "G", "O" ], [], [], [], [], []]

    #Creer une liste contenant tous les chiffres possibles dans un jeu de BINGO
    liste_chiffres = []
    chiffre = 1
    for n in range(len(liste)):
        liste_chiffres.append(chiffre)
        chiffre += 1

    #Séparer la liste de chiffres en sections selon leur lettre correspondante
    chiffres_b = liste_chiffres[0:15] #exemple: seuls les chiffres 1 à 15 se retrouvent sous la lettre 'B'
    chiffres_i = liste_chiffres[15:30]
    chiffres_n = liste_chiffres[30:45]
    chiffres_g = liste_chiffres[45:60]
    chiffres_o = liste_chiffres[60:]
    liste_chiffres = [chiffres_b, chiffres_i, chiffres_n, chiffres_g, chiffres_o]

    #choisir les chiffres aléatoirement et les ajouter dans la liste carte_joueur
    for i in range(len(liste_chiffres)):
        for j in range(len(liste_chiffres)):
            choix_random = random.choice(liste_chiffres[j])
            carte_joueur[i+1].append(choix_random)
            liste_chiffres[j].remove(choix_random)

    #Changer la case du milieu pour un espace libre
    carte_joueur[3].pop(2)
    carte_joueur[3].insert(2, "*")
    return carte_joueur

#Maryam
def placer_jeton(combi: str, grille: list[list[bool]], carte_joueur:str):
    """
    Fonction pour placer le jeton x sur la grille(liste2D) BINGO
    :param x: le jeton a placer sur la grille
    :param grille: la grille BINGO
    :param combi : combinaison
    :return: la carte bingo du joueur avec modification (jeton)
    """
    x = 'x'

    # Afficher le jeton sur la grille
    for x in grille:
        print(x)

    if combi in grille:
        return carte_joueur # nouvelle carte avec le jeton
    else:
        print("pas de combinaison valide pour ce tour ")
        return carte_joueur


"""
def remplacer_case(l: int, c: int, jeton: str, grille: list[list[str]]) -> None:

    Fonction pour remplacer les tirets par x ou o
    :param l: ligne
    :param c: colone
    :param jeton: x ou o
    :param grille: grille de tictactoe

    grille[l][c] = jeton

    #afficher la grille
    for ligne in grille:
        print(ligne)
"""

#Fonction qui détermine si on a une ligne BINGO gagnante
def bingo_gagnant(c_joueur :list[list]):
    """"
    Fonction qui détermine si on a une ligne BINGO gagnante
    :param colonne_gagnante:
    :param rangee_gagnate:
    :param c_joueur: la carte BINGO du oueur
    :return: "BINGO gagnant!" ou "Pas encore de BINGO."
    """
    x = "x"

    #Ligne Horizontale
    for i in range(5):
        if c_joueur[i][0] == str and c_joueur[i][1] == str and c_joueur[i][2] == str and c_joueur[i][3] == str and c_joueur[i][4] == str :
            colonne_gagnante = True
        else :
            colonne_gagnante = False


    #Ligne Vertical
    for i in range(5):
        if c_joueur[0][i] == str and c_joueur[1][i] == str and c_joueur[2][0] == str and c_joueur[3][0] == str and c_joueur[4][0] == str :
            rangee_gagnate = True
        else :
           rangee_gagnate = False

    #Ligne Diagonal gauche:
    if c_joueur[4][4] == str and c_joueur[3][3] == str and c_joueur[2][2] == str and c_joueur[1][1] == str and c_joueur[0][0] == str :
        diagonale_gagnante = True
    else:
        diagonale_gagnante = False

    #Ligne Diagonale droite:
    if c_joueur[0][5] == str and c_joueur[2][4] == str and c_joueur[3][3] == str and c_joueur[2][3]== str and c_joueur[1][4] :
        diagonale_gagnante = True
    else :
        diagonale_gagnante = False



     #Colonne Ganante
    if colonne_gagnante == True :
        return "BINGO gagant!"
    else :
        return "Pas encore de BINGO."
















"""
 bingo_gagnant()   #Appel de la fonction

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
        input() in grille
        print("Pas encore de BINGO.")
    else :
        print(x in combinaison_pigee)

    break
"""