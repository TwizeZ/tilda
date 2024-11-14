from linkedQFile import LinkedQ
import unittest

class Syntaxfel(Exception):
    pass

class SyntaxTest(unittest.TestCase):
    def testSyntax(self):
        korrektSyntax = ["Na","H2O", "Si(C3(COOH)2)4(H2O)7","Na332"]
        korrektOutput = "Formeln är syntaktiskt korrekt"
        for formel in korrektSyntax:
            self.assertEqual(Formel((formel)).resultat, korrektOutput)
    
    def testFelSyntax(self):
        felSyntax = ["C(Xx4)5","C(OH4)C","C(OH4C","H2O)Fe","H0","H1C","H02C","Nacl","a","(Cl)2)3",")","2"]
        felOutput =  [
            "Okänd atom vid radslutet 4)5",
            "Saknad siffra vid radslutet C",
            "Saknad högerparentes vid radslutet",
            "Felaktig gruppstart vid radslutet )Fe",
            "För litet tal vid radslutet ",
            "För litet tal vid radslutet C",
            "För litet tal vid radslutet 2C",
            "Saknad stor bokstav vid radslutet cl",
            "Saknad stor bokstav vid radslutet a",
            "Felaktig gruppstart vid radslutet )3",
            "Felaktig gruppstart vid radslutet )",
            "Felaktig gruppstart vid radslutet 2"]
        for formel, output in zip(felSyntax, felOutput):
            self.assertEqual(Formel((formel)).resultat, output)

ATOMER = [
    "H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne", "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar", 
    "K", "Ca", "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn", "Ga", "Ge", "As", "Se", "Br", 
    "Kr", "Rb", "Sr", "Y", "Zr", "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn", "Sb", "Te", 
    "I", "Xe", "Cs", "Ba", "La", "Ce", "Pr", "Nd", "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", 
    "Yb", "Lu", "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg", "Tl", "Pb", "Bi", "Po", "At", "Rn", 
    "Fr", "Ra", "Ac", "Th", "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm", "Md", "No", "Lr", 
    "Rf", "Db", "Sg", "Bh", "Hs", "Mt", "Ds", "Rg", "Cn", "Fl", "Lv"]

class Formel():
    def __init__(self, formel):
        self.formel = formel
        self.q = LinkedQ()
        self.bracketCounter = 0

        try:
            self.readFormel()
            self.resultat = "Formeln är syntaktiskt korrekt"
        except Syntaxfel as fel: 
            self.resultat = str(fel)
        
    def readFormel(self):
        for char in self.formel:
            if char == " ":
                continue
            self.q.enqueue(char)
        self.readMol()
        if self.bracketCounter > 0:
            raise Syntaxfel("Saknad högerparentes vid radslutet")
            
    def readMol(self):
        self.readGroup()
        if self.q.peek() is not None:
            self.readMol()

    def readGroup(self):
        if self.q.peek() is None:
            return
        
        if self.q.peek() == "(":
            self.bracketCounter += 1
            self.q.dequeue()
            self.readMol()
            return
            
        if self.q.peek() == ")" and self.bracketCounter > 0:
            self.bracketCounter -= 1
            self.q.dequeue()
            self.readNum()
            return
            
        if self.q.peek().isalpha():
            self.readAtom()
            if self.q.peek() is None:
                return
            if self.q.peek().isdigit():
                self.readNum()
            return

        raise Syntaxfel("Felaktig gruppstart vid radslutet " + self.emptyRest())
            
            
    def readAtom(self):
        atom = self.q.peek()      
        self.readLETTER()
        
        if self.q.peek() != None and self.q.peek().islower():
            atom += self.q.peek()
            self.readletter()
            
        if atom in ATOMER:
            return
        
        raise Syntaxfel("Okänd atom vid radslutet " + self.emptyRest())
        
    def readLETTER(self):
        LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        letter = self.q.peek()
        if letter in LETTERS:
            self.q.dequeue()
            return
        
        raise Syntaxfel("Saknad stor bokstav vid radslutet " + self.emptyRest())

    def readletter(self):
        letters = "abcdefghijklmnopqrstuvwxyz"
        letter = self.q.dequeue()
        if letter in letters:
            return
        
    def readNum(self):
        if self.q.peek() == None or not self.q.peek().isdigit():
            raise Syntaxfel("Saknad siffra vid radslutet " + self.emptyRest())
        
        numStr = self.q.dequeue()

        while not self.q.peek() == None and self.q.peek().isdigit():
            numStr += self.q.dequeue()

        if numStr[0] == "0" or int(numStr) < 2:
            raise Syntaxfel("För litet tal vid radslutet " + numStr[1:] + self.emptyRest())

    def emptyRest(self):
        rest = ""
        while not self.q.isEmpty():
            rest += self.q.dequeue()
        return rest
     
def main():
    formel = input()
    while formel != "#":
        molformel = Formel(formel)
        print(molformel.resultat)
        formel = input()

if __name__ == "__main__":
    main()
    unittest.main()