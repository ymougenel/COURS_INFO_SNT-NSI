import unittest
import jeu


class Testjeu(unittest.TestCase):

    def setUp(self):
        jeu.init_partie()

    def test_lecture_ecriture_plateau(self):
        for i in range(3):
            for j in range(3):
                self.assertEqual("", jeu.lire_plateau(0, 0))

        jeu.ecrire_plateau(0, 0, "X")
        jeu.ecrire_plateau(1, 1, "O")
        jeu.ecrire_plateau(2, 1, "Y")

        self.assertEqual("X", jeu.lire_plateau(0, 0))
        self.assertEqual("O", jeu.lire_plateau(1, 1))
        self.assertEqual("Y", jeu.lire_plateau(2, 1))

    def test_demander_noms_joueurs(self):
        __builtins__.input = lambda _: 'Yann'
        jeu.demander_noms_joueurs()
        self.assertEqual(jeu.nom_joueur1, "Yann")
        self.assertEqual(jeu.nom_joueur2, "Yann")

    def test_demander_valeur(self):
        __builtins__.input = lambda _: 'Yann'
        jeu.demander_noms_joueurs()
        self.assertEqual(jeu.nom_joueur1, "Yann")
        self.assertEqual(jeu.nom_joueur2, "Yann")

if __name__ == '__main__':
    unittest.main()
