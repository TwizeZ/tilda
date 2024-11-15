import unittest

from syntax import kollaMolekyl


class SyntaxTest(unittest.TestCase):

    def testMolekyl(self):
        self.assertEqual(kollaMolekyl("Na"), "Formeln är syntaktiskt korrekt")

    def testMolekyl2(self):
        self.assertEqual(kollaMolekyl("H2O"), "Formeln är syntaktiskt korrekt")

    def testMolekyl3(self):
        self.assertEqual(kollaMolekyl("Si(C3(COOH)2)4(H2O)7"), "Formeln är syntaktiskt korrekt")

    def testMolekyl4(self):
        self.assertEqual(kollaMolekyl("Na332"), "Formeln är syntaktiskt korrekt")

if __name__ == '__main__':
    unittest.main()