#Plan de test pour la fonction generer_carte()
#^^^^Vérifier la longueur de la liste

#Plan de test pour la fonction creer_liste_combinaisons()

#Plan de test pour la fonction placer_jeton()

| combinaison pigée | carte_joueur                                   | resultat_attendu                                  | resultat_obtenu |
|-------------------|------------------------------------------------|---------------------------------------------------|-----------------|
| B-12              | (B-12 existe dans la liste carte_joueur)       | carte joueur avec l'espace B-12 remplacé par un x |                 |
| B-12              | (B-12 n'existe pas dans la liste carte_joueur) | carte joueur inchangée                            |                 |
| G-55              | (G-55 existe dans la liste carte_joueur)       | carte joueur avec l'espace G-55 remplacé par un x |                 |


#Plan de test pour la fonction bingo_gagnant()

| carte_joueur                                      | resultat_attendu        | resultat_obtenu |
|---------------------------------------------------|-------------------------|-----------------|
| (ligne horizontale remplie de str)                | "BINGO gagnant!"        |                 |
| (ligne verticale remplie de str)                  | "BINGO gagnant!"        |                 |
| (ligne diagonale remplie de str, gauche à droite) | "BINGO gagnant!"        |                 |
| (ligne diagonale remplie de str, droite à gauche) | "BINGO gagnant!"        |                 |
| (Aucune de ces options)                           | "Pas encore de BINGO."  |                 |