"""
Felix Larsson
Labbpartner: Anton Kancans
DD1320 Tillämpad datalogi
Labb 10
2024-11-15
"""

from linkedQFile import LinkedQ
from molgrafik import *
from hashtest import *


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
        current = mol  # Start with the first group

        while self.q.peek() not in [".", ")"]:
            # Read the next group and chain it to the current molecule
            next_mol = self.readGroup()
            current.next = next_mol  # Link to the next group
            current = next_mol       # Move to the newly added group

        if self.q.peek() == ")":
            return mol  # Ends the current molecule if ")" is reached

        if self.brackets != 0:
            raise Syntaxfel("Saknad högerparentes vid radslutet ")
        
        return mol


    def readGroup(self):
        rutan = Ruta()

        if self.q.peek().isalpha():  # If the group starts with an atom
            rutan.atom = self.readAtom()
            if self.q.peek().isdigit():  # Check for numeric subscript
                rutan.num = self.readNum()

        elif self.q.peek() == "(":  # If the group starts with "("
            self.brackets += 1
            self.q.dequeue()  # Remove "("
            rutan.down = self.readMolekyl()  # Process the nested molecule

            if self.q.peek() != ")":
                raise Syntaxfel("Saknad högerparentes vid radslutet ")

            self.brackets -= 1
            self.q.dequeue()  # Remove ")"
            
            if self.q.peek().isdigit():
                rutan.num = self.readNum()  # Get the multiplier for the nested group
            else:
                raise Syntaxfel("Saknad siffra vid radslutet ")

        elif self.q.peek() == ")" and self.brackets > 0:  # Closing bracket for nested group
            self.brackets -= 1
            self.q.dequeue()  # Remove ")"
            if self.q.peek().isdigit():
                rutan.num = self.readNum()
            else:
                raise Syntaxfel("Saknad siffra vid radslutet ")

        else:
            raise Syntaxfel("Felaktig gruppstart vid radslutet ")
        
        return rutan

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
            return letter
        raise Syntaxfel("Saknad stor bokstav vid radslutet " + letter)


    def readLetter(self):
        if self.q.peek() in "abcdefghijklmnopqrstuvwxyz":
            letter = self.q.dequeue()
            return letter
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



def weight(mol):
    atom_list = skapaAtomlista()
    atom_table = lagraHashtabell(atom_list)

    if mol.down is not None:    # Om rutan man är på är en parantes, ta det nedanför gånger siffran
        vikt = weight(mol.down) * mol.num

    else:
        if mol.num is not None:     # Om siffran är större än 1
            vikt = atom_table[mol.atom].vikt * mol.num
        else:
            vikt = atom_table[mol.atom].vikt

    if mol.next is not None:    # Om det finns något på next, lägg till den vikten
        vikt += weight(mol.next)

    return vikt


def addMolekyl(molecule):
    q = LinkedQ()
    for character in molecule:
        q.enqueue(character)
    q.enqueue(".")
    formel = Formel(q)
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
        # print(weight(resultat))
        mg.show(resultat)
        molekyl = input()
    print()


if __name__ == "__main__":
    main()