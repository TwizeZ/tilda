"""
Felix Larsson
Labbpartner: Anton Kancans
DD1320 Tillämpad datalogi
Labb 10
2024-11-15
"""

from linkedQFile import LinkedQ
from molgrafik import *


class Syntaxfel(Exception):
    pass


class Formel():
    def __init__(self, formel):
        self.q = formel
        self.brackets = 0


    def isAtom(self, atom):
        atoms = """H   He  Li  Be  B   C   N   O   F   Ne  Na  Mg  Al  Si  P   S   Cl  Ar  K   Ca  Sc  Ti  V   Cr
                    Mn  Fe  Co  Ni  Cu  Zn  Ga  Ge  As  Se  Br  Kr  Rb  Sr  Y   Zr  Nb  Mo  Tc  Ru  Rh  Pd  Ag  Cd
                    In  Sn  Sb  Te  I   Xe  Cs  Ba  La  Ce  Pr  Nd  Pm  Sm  Eu  Gd  Tb  Dy  Ho  Er  Tm  Yb  Lu  Hf
                    Ta  W   Re  Os  Ir  Pt  Au  Hg  Tl  Pb  Bi  Po  At  Rn  Fr  Ra  Ac  Th  Pa  U   Np  Pu  Am  Cm
                    Bk  Cf  Es  Fm  Md  No  Lr  Rf  Db  Sg  Bh  Hs  Mt  Ds  Rg  Cn  Fl  Lv""".split()
        
        if atom in atoms:
            return True
        else:
            return False


    def readFormel(self):
        return self.readMolekyl()


    def readMolekyl(self):
        mol = self.readGroup()
        if self.q.peek() != ".":                                            # Om det inte är slutet på molekylen
            mol.next = self.readMolekyl()
        if self.brackets != 0:                                              # Om det inte är lika många vänster- som högerparenteser
            raise Syntaxfel("Saknad högerparentes vid radslutet ")
        return mol
        

    def readGroup(self):
        rutan = Ruta()

        if self.q.peek().isalpha():                                         # Om det är en bokstav
            rutan.atom = self.readAtom()
            if self.q.peek().isdigit():                                     # Om det kommer en siffra efter bokstaven
                rutan.num = self.readNum()

        elif self.q.peek() == "(":                                          # Om det är en vänsterparentes
            self.brackets += 1
            self.q.dequeue()
            while self.q.peek() != "." and self.q.peek() != ")":
               rutan.down = self.readMolekyl()

        elif self.q.peek() == ")" and self.brackets != 0:                   # Om det är en högerparentes
            self.brackets -= 1
            self.q.dequeue()
            if self.q.peek().isdigit():
                rutan.num = self.readNum()
            else:
                raise Syntaxfel("Saknad siffra vid radslutet ")

        else:
            raise Syntaxfel("Felaktig gruppstart vid radslutet ")
        return rutan                                                        # Returnera i if-satserna? Eller någon annanstans?


    def readAtom(self):
        atom = self.readLETTER()

        if self.q.peek().isdigit() and self.isAtom(atom):                   # Om det är en siffra efter, och om det är en atom
            return atom
        
        elif self.q.peek().islower():                                       # Om det är en liten bokstav
            atom += self.readLetter()
            if self.isAtom(atom):
                return atom
            else:
                raise Syntaxfel("Okänd atom vid radslutet ")
            
        elif self.isAtom(atom):                                             # Om det inte är en liten bokstav eller siffra, men det är en atom
            return atom
        
        else:                                                               # Om det inte är en atom
            raise Syntaxfel("Okänd atom vid radslutet ")


    def readLETTER(self):
        letter = self.q.dequeue()

        if letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            return(letter)
        raise Syntaxfel("Saknad stor bokstav vid radslutet " + letter)


    def readLetter(self):
        if self.q.peek() in "abcdefghijklmnopqrstuvwxyz":
            letter = self.q.dequeue()
            return(letter)
        return


    def readNum(self):
        number = int(self.q.dequeue())
        if number == 0:
            raise Syntaxfel("För litet tal vid radslutet ")
        while self.q.peek().isdigit():
            number = number * 10 + int(self.q.dequeue())
        if number > 1:
            return number
        elif number < 2:
            raise Syntaxfel("För litet tal vid radslutet ")


def addMolekyl(molecule):
    q = LinkedQ()
    for character in molecule:
        q.enqueue(character)
    q.enqueue(".")
    formel = Formel(q)
    print(formel)
    return formel


def kollaMolekyl(molekyl):
    formel = addMolekyl(molekyl)
    
    try:
        result = formel.readFormel()
        print("Formeln är syntaktiskt korrekt")
        return result
    except Syntaxfel as fel:
        kvar = ""
        while not formel.q.isEmpty():
            char = formel.q.dequeue()
            if char != ".":
                kvar += char
        return str(fel) + kvar


def main():
    mg = Molgrafik() 
    molekyl = input()
    while not molekyl == "#":
        resultat = kollaMolekyl(molekyl)
        print(resultat)
        mg.show(resultat)
        molekyl = input()


if __name__ == "__main__":
    main()