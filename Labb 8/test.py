"""
Felix Larsson
Labbpartner: Anton Kancans
DD1320 Tillämpad datalogi
Labb 8
2024-11-01
"""

from syntax import *
import unittest

#######################################################################
#       Testerna
#######################################################################

class TestMoleculeSyntax(unittest.TestCase):

    def test_valid_molecule(self):
        print("\nTesting a valid molecule")
        molecule = "H2O"
        result = kollaSyntax(molecule)
        self.assertEqual(result, "Formeln är syntaktiskt korrekt")

    def test_invalid_molecule_missing_capital(self):
        print("\nTesting molecule with missing capital letter")
        molecule = "h2O"  # Invalid due to lowercase start
        result = kollaSyntax(molecule)
        self.assertTrue("Syntaxfel: Saknad stor bokstav vid radslutet" in result)

    def test_invalid_molecule_incorrect_number(self):
        print("\nTesting molecule with invalid number")
        molecule = "H1"  # Invalid due to number < 2
        result = kollaSyntax(molecule)
        self.assertTrue("För litet tal vid radslut" in result)

    def test_molecule_with_lowercase_letter(self):
        print("\nTesting molecule with lowercase letter following uppercase")
        molecule = "He2"  # Should be valid
        result = kollaSyntax(molecule)
        self.assertEqual(result, "Formeln är syntaktiskt korrekt")

    def test_molecule_with_long_atom_names(self):
        print("\nTesting molecule with two-letter atom")
        molecule = "Mg12"
        result = kollaSyntax(molecule)
        self.assertEqual(result, "Formeln är syntaktiskt korrekt")

    def test_invalid_syntax_too_small_number(self):
        print("\nTesting molecule with number too small")
        molecule = "C1"
        result = kollaSyntax(molecule)
        self.assertTrue("För litet tal vid radslut" in result)

    def test_invalid_syntax_missing_number(self):
        print("\nTesting molecule missing number after atom")
        molecule = "O"
        result = kollaSyntax(molecule)
        self.assertEqual(result, "Formeln är syntaktiskt korrekt")

    def test_invalid_syntax_missing_capital(self):
        print("\nTesting molecule with only small characters")
        molecule = "cr12"
        result = kollaSyntax(molecule)
        self.assertTrue("Syntaxfel" in result)

#######################################################################
#       Main Execution
#######################################################################

if __name__ == "__main__":
    unittest.main()