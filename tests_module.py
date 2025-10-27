import pytest
from module import *

#test pour la fonction placer_jeton()
def test_placer_jeton1(combi, carte, reponse_lettre, reponse_ligne, resultat_attendu):
    #Arrange
    combi = "B-12"
    carte = [['B', 'I', 'N', 'G', 'O'],
             [8, 30, 33, 58, 65],
             [12, 17, 45, 51, 62],
             [15, 23, '*', 46, 74],
             [10, 26, 31, 55, 66],
             [3, 27, 32, 57, 61]]
    reponse_lettre = "B"
    reponse_ligne = 2
    resultat_attendu = [['B', 'I', 'N', 'G', 'O'],
             [8, 30, 33, 58, 65],
             ['x', 17, 45, 51, 62],
             [15, 23, '*', 46, 74],
             [10, 26, 31, 55, 66],
             [3, 27, 32, 57, 61]]
    #Act
    resultat_obtenu = placer_jeton(combi, carte)

    #Assert
    assert resultat_obtenu == resultat_attendu

    #Assert
    assert resultat_obtenu == resultat_attendu
#test pour la fonction bingo_gagnant()
@pytest.mark.parametrize("carte_joueur, resultat_attendu", [
    ([['B', 'I', 'N', 'G', 'O'],
     [8, 30, 33, 58, 65],
     [12, 17, 45, 51, 62],
     ['x','x', '*', 'x', 'x'],
     [10, 26, 31, 55, 66],
     [3, 27, 32, 57, 61]], "BINGO gagnant!"),

    ([['B', 'I', 'N', 'G', 'O'],
     [8, 30, 33, 'x', 65],
     [12, 17, 45, 'x', 62],
     [7, 23, '*', 'x', 74],
     [10, 26, 31, 'x', 66],
     [3, 27, 32, 'x', 61]], "BINGO gagnant!"),

    ([['B', 'I', 'N', 'G', 'O'],
     ['x', 30, 33, 58, 65],
     [12, 'x', 45, 51, 62],
     [7, 23, '*', 56, 70],
     [10, 26, 31, 'x', 66],
     [3, 27, 32, 57, 'x']], "BINGO gagnant!"),

    ([['B', 'I', 'N', 'G', 'O'],
     [8, 30, 33, 58, 'x'],
     [12, 17, 45, 'x', 62],
     [7, 23, '*', 56, 70],
     [10, 'x', 31, 55, 66],
     ['x', 27, 32, 57, 61]], "BINGO gagnant!"),

    ([['B', 'I', 'N', 'G', 'O'],
     [8, 'x', 33, 58, 65],
     [12, 17, 45, 'x', 62],
     [7, 23, '*', 56, 70],
     [10, 26, 31, 55, 66],
     [3, 27, 32, 57, 61]], "Pas encore de BINGO."),
])

def test_bingo_gagnant(carte_joueur, resultat_attendu):
    #Act
    resultat_obtenu = bingo_gagnant(carte_joueur)

    #Asssert
    assert resultat_obtenu == resultat_attendu