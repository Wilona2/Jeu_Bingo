#Plan de test pour la fonction generer_carte()

#Plan de test pour la fonction creer_liste_combinaisons()

#Plan de test pour la fonction placer_jeton()

| combinaison_pigee | carte_joueur                                           | réponse_joueur | resultat_attendu                                 | resultat_obtenu |
|-------------------|--------------------------------------------------------|----------------|--------------------------------------------------|-----------------|
| B-12              | (B-12 existe dans la liste carte_joueur, à la ligne 2) | B, 2           | (le chiffre à l'espace B2 est remplacé par un x) |                 |
| B-12              | (B-12 existe dans la liste carte_joueur, à la ligne 2) | B, 3           | Message d'erreur                                 |                 |
| B-12              | (B-12 n'existe pas dans la liste carte_joueur)         | B, 3           | Message d'erreur                                 |                 |
| B-12              | (B-12 n'existe pas dans la liste carte_joueur)         | x              | (on affiche la carte_joueur inchangée)           |                 |
| B-12              | (B-12 existe dans la carte_joueur)                     | x              | Message d'erreur                                 |                 |

#Plan de test pour la fonction bingo_gagnant()

| carte_joueur                                      | resultat_attendu        | resultat_obtenu |
|---------------------------------------------------|-------------------------|-----------------|
| (ligne horizontale remplie de str)                | "BINGO gagnant!"        |                 |
| (ligne verticale remplie de str)                  | "BINGO gagnant!"        |                 |
| (ligne diagonale remplie de str, gauche à droite) | "BINGO gagnant!"        |                 |
| (ligne diagonale remplie de str, droite à gauche) | "BINGO gagnant!"        |                 |
| (Aucune de ces options)                           | "Pas encore de BINGO."  |                 |