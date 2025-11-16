#Plan de test pour la fonction generer_carte()
#^^^^Vérifier la longueur de la liste

| Carte aléatoire | carte_joueur | resultat_attendu | resultat_obtenu |
|-----------------|--------------|------------------|-----------------|
|                 |              |                  |                 |
|                 |              |                  |                 |
|                 |              |                  |                 |


#Plan de test pour la fonction creer_liste_combinaisons()

| liste combinaison             | resultat_attendu | resultat_obtenu |
|-------------------------------|------------------|-----------------|
| combinaison aléatoire ligne B | B: 1-15          | "B-3"           |
| combinaison aléatoire ligne I | I: 16-30         | "I-22"          |
| combinaison aléatoire ligne N | N:  31-45        | "N-36"          |
| combinaison aléatoire ligne G | G: 46-60         | "G-54"          |
| combinaison aléatoire ligne O | O: 61-72         | "O-70"          |


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