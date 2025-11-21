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
    #liste_chiffres = list(range(1, 76))
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
def placer_jeton(combi: str, carte_joueur : list[list])-> list[list]:
    """
    Fonction pour placer le jeton x sur la grille(liste2D) BINGO
    :param carte_joueur: la grille BINGO
    :param combi : combinaison
    :return: la carte bingo du joueur avec modification (jeton)
    """
    combi = combi.split("-")
    combi.pop(0)
    combi = int(combi[0])
    print(combi)

    # Afficher le jeton sur la grille

    
    for i in range(5):  # lignes
        for j in range(5):  # Colonnes
            if combi == carte_joueur[i][j]:  # Si la valeur est la même
                carte_joueur[i][j] = 'x'  # Remplacer par X


    """
    index = 0
    for i in range(len(carte_joueur)):
        if combi in carte_joueur[i]:
            
            carte_joueur[i][j] = 'x'
        index += 1
    """
    """
                for i in range(len(carte_joueur)):
        for j in range(len(carte_joueur[i])):
            if carte_joueur == combi:
                carte_joueur[i][j] = 'x'
                print(carte_joueur[i][j])
    """

    return carte_joueur

#Maryam
def bingo_gagnant(c_joueur :list[list]):
    """"
    Fonction qui détermine si on a une ligne BINGO gagnante
    :param c_joueur: la carte BINGO du joueur
    :return: "BINGO gagnant!" ou "Pas encore de BINGO."
    """
    sous_colonne = [l for l in range (list)]
    for list in c_joueur[1:]:
        for i in range(len(list)):
            if
    # verifier que list[i] == x pour toute list et i fixe
    """
    #Ligne Horizontale
    for i in range(5):
        if c_joueur[i][1] == "x" and c_joueur[i][2] == "x" and c_joueur[i][3] == "x" and c_joueur[i][4] == "x"  :
            colonne_gagnante = True
    """

    """
    #Ligne Vertical
    for i in range(5):
        if c_joueur[1][i] == "x" and c_joueur[2][i] == "x" and c_joueur[3][0] == "x" and c_joueur[4][0] == "x" and c_joueur[5][0] == "x" :
            colonne_gagnante = True
    """
    """
        elif all(c_joueur[i]== "x" for i in range(5)):
            return True
    """
    """
    #Ligne Diagonal gauche:
    if c_joueur[5][0] == "x" and c_joueur[4][1] == "x" and c_joueur[3][2] == "x" and c_joueur[2][3] == "x" and c_joueur[1][4] == "x" :
        colonne_gagnante = True


    #Ligne Diagonale droite:
    if c_joueur[5][4] == "x" and c_joueur[4][3] == "x" and c_joueur[3][2] == "x" and c_joueur[2][1]== "x" and c_joueur[1][1] :
        colonne_gagnante = True

    colonne_gagnante    = True
    
    #Colonne Ganante
    if colonne_gagnante == True :
        return "BINGO gagant!"
    else :
        return "Pas encore de BINGO."
    """