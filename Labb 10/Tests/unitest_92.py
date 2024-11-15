import unittest

from syntax import kollaMolekyl


class SyntaxTest(unittest.TestCase):

    def testOkandAtom(self):
        self.assertEqual(kollaMolekyl("C(Xx4)5"), "Okänd atom vid radslutet 4)5")

    def testSaknadSiffra(self):
        self.assertEqual(kollaMolekyl("C(OH4)C"), "Saknad siffra vid radslutet C")

    def testSaknadHogerParantes(self):                                                           # FAIL
        self.assertEqual(kollaMolekyl("C(OH4C"), "Saknad högerparentes vid radslutet ")

    def testFelGruppstart(self):
        self.assertEqual(kollaMolekyl("H2O)Fe"), "Felaktig gruppstart vid radslutet )Fe")

    def testLitetTal(self):
        self.assertEqual(kollaMolekyl("H0"), "För litet tal vid radslutet ")

    def testLitetTal2(self):
        self.assertEqual(kollaMolekyl("H1C"), "För litet tal vid radslutet C")

    def testLitetTal3(self):
        self.assertEqual(kollaMolekyl("H02C"), "För litet tal vid radslutet 2C")

    def testSaknadStorBokstav(self):
        self.assertEqual(kollaMolekyl("Nacl"), "Saknad stor bokstav vid radslutet cl")

    def testSaknadStorBokstav2(self):
        self.assertEqual(kollaMolekyl("a"), "Saknad stor bokstav vid radslutet a")

    def testFelGruppstart2(self):
        self.assertEqual(kollaMolekyl("(Cl)2)3"), "Felaktig gruppstart vid radslutet )3")

    def testFelGruppstart3(self):
        self.assertEqual(kollaMolekyl(")"), "Felaktig gruppstart vid radslutet )")

    def testFelGruppstart4(self):
        self.assertEqual(kollaMolekyl("2"), "Felaktig gruppstart vid radslutet 2")



if __name__ == '__main__':
    unittest.main()