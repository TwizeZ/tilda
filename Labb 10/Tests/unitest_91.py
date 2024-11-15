import unittest

from syntax import kollaMolekyl
from molgrafik import Ruta


class SyntaxTest(unittest.TestCase):

    def testMolekyl(self):
        result = kollaMolekyl("Na")
        self.assertIsInstance(result, Ruta)
        self.assertEqual(result.atom, "Na")
        self.assertEqual(result.num, 1)

    def testMolekyl2(self):
        result = kollaMolekyl("H2O")
        self.assertIsInstance(result, Ruta)
        self.assertEqual(result.atom, "H")
        self.assertEqual(result.num, 2)
        self.assertIsNotNone(result.next)
        self.assertEqual(result.next.atom, "O")
        self.assertEqual(result.next.num, 1)

    def testMolekyl3(self):
        result = kollaMolekyl("Si(C3(COOH)2)4(H2O)7")
        self.assertIsInstance(result, Ruta)
        self.assertEqual(result.atom, "Si")
        self.assertEqual(result.num, 1)
        self.assertIsNotNone(result.down)
        self.assertEqual(result.down.atom, "C")
        self.assertEqual(result.down.num, 3)

    def testMolekyl4(self):
        result = kollaMolekyl("Na332")
        self.assertIsInstance(result, Ruta)
        self.assertEqual(result.atom, "Na")
        self.assertEqual(result.num, 332)


if __name__ == '__main__':
    unittest.main()