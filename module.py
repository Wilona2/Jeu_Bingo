import random
#Wilo
def creer_liste_combinaisons() -> list:
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
def generer_carte(liste: list) -> list:
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
    chiffres_b = liste_chiffres[0:15] #ex: seuls les chiffres 1 à 15 se retrouvent sous la lettre 'B'
    chiffres_i = liste_chiffres[15:30]
    chiffres_n = liste_chiffres[31:45]
    chiffres_g = liste_chiffres[45:60]
    chiffres_o = liste_chiffres[60:]
    liste_chiffres = [chiffres_b, chiffres_i, chiffres_n, chiffres_g, chiffres_o]

    #choisir les chiffres aléatoirement et les ajouter dans la liste carte_joueur
    index = 1
    for i in range(len(liste_chiffres)):
        for j in range(len(liste_chiffres)):
            choix_random = random.choice(liste_chiffres[j])
            carte_joueur[index].append(choix_random)
            liste_chiffres[j].remove(choix_random)
        index += 1 #passer à la prochaine ligne de la carte joueur

    #Changer la case du milieu pour un espace libre
    carte_joueur[3].pop(2)
    carte_joueur[3].insert(2, "*")
    return carte_joueur

#test
liste_combinaisons = creer_liste_combinaisons()
carte_j = generer_carte(liste_combinaisons)
for ligne in carte_j:
    print(ligne)