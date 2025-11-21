from tkinter import Listbox

import pytest
from module import *


#test pour la fonction placer_jeton()
def test_placer_jeton1():
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


def test_placer_jeton2():
    # Arrange
    combi = "B-12"
    carte = [['B', 'I', 'N', 'G', 'O'],
             [8, 30, 33, 58, 65],
             [12, 17, 45, 51, 62],
             [15, 23, '*', 46, 74],
             [10, 26, 31, 55, 66],
             [3, 27, 32, 57, 61]]
    reponse_lettre = "B"
    reponse_ligne = 3
    resultat_attendu = [['B', 'I', 'N', 'G', 'O'],
                        [8, 30, 33, 58, 65],
                        ['x', 17, 45, 51, 62],
                        [15, 23, '*', 46, 74],
                        [10, 26, 31, 55, 66],
                        [3, 27, 32, 57, 61]]  #avec message d'erreur
    # Act
    resultat_obtenu = placer_jeton(combi, carte)
    # Assert
    assert resultat_obtenu == resultat_attendu


def test_placer_jeton3():
    # Arrange
    combi = "B-12"
    carte = [['B', 'I', 'N', 'G', 'O'],
             [8, 30, 33, 58, 65],
             [6, 17, 45, 51, 62],
             [15, 23, '*', 46, 74],
             [10, 26, 31, 55, 66],
             [3, 27, 32, 57, 61]]
    reponse_lettre = "B"
    reponse_ligne = 3
    resultat_attendu = [['B', 'I', 'N', 'G', 'O'],
                        [8, 30, 33, 58, 65],
                        [6, 17, 45, 51, 62],
                        [15, 23, '*', 46, 74],
                        [10, 26, 31, 55, 66],
                        [3, 27, 32, 57, 61]]  #avec message d'erreur
    # Act
    resultat_obtenu = placer_jeton(combi, carte)
    # Assert
    assert resultat_obtenu == resultat_attendu


def test_placer_jeton4():
    # Arrange
    combi = "B-12"
    carte = [['B', 'I', 'N', 'G', 'O'],
             [8, 30, 33, 58, 65],
             [6, 17, 45, 51, 62],
             [15, 23, '*', 46, 74],
             [10, 26, 31, 55, 66],
             [3, 27, 32, 57, 61]]
    reponse_lettre = "x"
    resultat_attendu = [['B', 'I', 'N', 'G', 'O'],
                        [8, 30, 33, 58, 65],
                        [6, 17, 45, 51, 62],
                        [15, 23, '*', 46, 74],
                        [10, 26, 31, 55, 66],
                        [3, 27, 32, 57, 61]]
    # Act
    resultat_obtenu = placer_jeton(combi, carte)
    # Assert
    assert resultat_obtenu == resultat_attendu


def test_placer_jeton5():
    # Arrange
    combi = "B-12"
    carte = [['B', 'I', 'N', 'G', 'O'],
             [8, 30, 33, 58, 65],
             [12, 17, 45, 51, 62],
             [15, 23, '*', 46, 74],
             [10, 26, 31, 55, 66],
             [3, 27, 32, 57, 61]]
    reponse_lettre = "x"
    resultat_attendu = [['B', 'I', 'N', 'G', 'O'],
                        [8, 30, 33, 58, 65],
                        ['x', 17, 45, 51, 62],
                        [15, 23, '*', 46, 74],
                        [10, 26, 31, 55, 66],
                        [3, 27, 32, 57, 61]]  #avec message d'erreur
    # Act
    resultat_obtenu = placer_jeton(combi, carte)
    # Assert
    assert resultat_obtenu == resultat_attendu


#test pour la fonction bingo_gagnant()
@pytest.mark.parametrize("carte_joueur, resultat_attendu", [
    ([['B', 'I', 'N', 'G', 'O'],
      [8, 30, 33, 58, 65],
      [12, 17, 45, 51, 62],
      ['x', 'x', '*', 'x', 'x'],
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

    # le <x> se trouve a la position (1, 0)
    # Verifier colonne
    """
    
    """
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

    # Verifier qu'on a <X> sur une ligne, une colonne ou une diagonale

    #Asssert
    assert resultat_obtenu == resultat_attendu


def test_creer_liste_combinaison(carte_joueur):
    #Arrange
    #combi = "B-9"
    carte_joueur = ([['B', 'I', 'N', 'G', 'O'],
                     [6, 30, 33, 58, 65],
                     [12, 21, 45, 51, 62],
                     [7, 23, '*', 56, 70],
                     [10, 26, 31, 55, 66],
                     [3, 27, 32, 57, 61]])
    resultat_attendu = ([['B', 'I', 'N', 'G', 'O'],
                         [6, 30, 33, 58, 65],
                         [12, 21, 45, 51, 62],
                         [7, 23, '*', 56, 70],
                         [10, 26, 31, 55, 66],
                         [3, 27, 32, 57, 61]], "B-9")

    # Act
    resultat_obtenu = creer_liste_combinaisons()

    # Assert
    assert resultat_obtenu == resultat_attendu


def test_generer_carte1():
    #Arrange
    carte_joueur = [['B', 'I', 'N', 'G', 'O'],
                    [8, 30, 33, 58, 65],
                    [12, 17, 45, 51, 62],
                    [15, 23, '*', 46, 74],
                    [10, 26, 31, 55, 66],
                    [3, 27, 32, 57, 61]]

    resultat_attendu = carte_joueur
    #Act
    resultat_obtenu = generer_carte(carte_joueur)
    #Assert
    assert resultat_obtenu == resultat_attendu
