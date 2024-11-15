import unittest

from syntax import kollaMolekyl


class SyntaxTest(unittest.TestCase):

    def testOkandAtom(self):
        mol = "C(Xx4)5"
        output = "Okänd atom vid radslutet 4)5"
        result = kollaMolekyl(mol)
        self.assertIsInstance(result, str)
        self.assertTrue(output in result)

    def testSaknadSiffra(self):
        mol = "C(OH4)C"
        output = "Saknad siffra vid radslutet C"
        result = kollaMolekyl(mol)
        self.assertIsInstance(result, str)
        self.assertTrue(output in result)

    def testSaknadHogerParantes(self):
        mol = "C(OH4C"
        output = "Saknad högerparentes vid radslutet"
        result = kollaMolekyl(mol)
        self.assertIsInstance(result, str)
        self.assertTrue(output in result)

    def testFelGruppstart(self):
        mol = "H2O)Fe"
        output = "Felaktig gruppstart vid radslutet )Fe"
        result = kollaMolekyl(mol)
        self.assertIsInstance(result, str)
        self.assertTrue(output in result)

    def testLitetTal(self):
        mol = "H0"
        output = "För litet tal vid radslutet "
        result = kollaMolekyl(mol)
        self.assertIsInstance(result, str)
        self.assertTrue(output in result)

    def testLitetTal2(self):
        mol = "H1C"
        output = "För litet tal vid radslutet C"
        result = kollaMolekyl(mol)
        self.assertIsInstance(result, str)
        self.assertTrue(output in result)

    def testLitetTal3(self):
        mol = "H02C"
        output = "För litet tal vid radslutet 2C"
        result = kollaMolekyl(mol)
        self.assertIsInstance(result, str)
        self.assertTrue(output in result)

    def testSaknadStorBokstav(self):
        mol = "Nacl"
        output = "Saknad stor bokstav vid radslutet cl"
        result = kollaMolekyl(mol)
        self.assertIsInstance(result, str)
        self.assertTrue(output in result)

    def testSaknadStorBokstav2(self):
        mol = "a"
        output = "Saknad stor bokstav vid radslutet a"
        result = kollaMolekyl(mol)
        self.assertIsInstance(result, str)
        self.assertTrue(output in result)

    def testFelGruppstart2(self):
        mol = "(Cl)2)3"
        output = "Felaktig gruppstart vid radslutet )3"
        result = kollaMolekyl(mol)
        self.assertIsInstance(result, str)
        self.assertTrue(output in result)

    def testFelGruppstart3(self):
        mol = ")"
        output = "Felaktig gruppstart vid radslutet )"
        result = kollaMolekyl(mol)
        self.assertIsInstance(result, str)
        self.assertTrue(output in result)

    def testFelGruppstart4(self):
        mol = "2"
        output = "Felaktig gruppstart vid radslutet 2"
        result = kollaMolekyl(mol)
        self.assertIsInstance(result, str)
        self.assertTrue(output in result)



if __name__ == '__main__':
    unittest.main()