"""
Felix Larsson
Labbpartner: Anton Kancans
DD1320 Tillämpad datalogi
Labb 9
2024-11-08
"""

from linkedQFile import LinkedQ


class Syntaxfel(Exception):
    pass


class Formel():
    def __init__(self, formel):
        self.q = formel
        self.brackets = 0


    def isAtom(self, atom):
        atomes = """H   He  Li  Be  B   C   N   O   F   Ne  Na  Mg  Al  Si  P   S   Cl  Ar  K   Ca  Sc  Ti  V   Cr
    Mn  Fe  Co  Ni  Cu  Zn  Ga  Ge  As  Se  Br  Kr  Rb  Sr  Y   Zr  Nb  Mo  Tc  Ru  Rh  Pd  Ag  Cd
    In  Sn  Sb  Te  I   Xe  Cs  Ba  La  Ce  Pr  Nd  Pm  Sm  Eu  Gd  Tb  Dy  Ho  Er  Tm  Yb  Lu  Hf
    Ta  W   Re  Os  Ir  Pt  Au  Hg  Tl  Pb  Bi  Po  At  Rn  Fr  Ra  Ac  Th  Pa  U   Np  Pu  Am  Cm
    Bk  Cf  Es  Fm  Md  No  Lr  Rf  Db  Sg  Bh  Hs  Mt  Ds  Rg  Cn  Fl  Lv""".split()
        if atom in atomes:
            return True
        else:
            return False


    def readFormel(self):
        self.readMolekyl()
        return "Formeln är syntaktiskt korrekt"


    def readMolekyl(self):
        self.readGroup()
        if self.q.peek() != ".":
            self.readMolekyl()
        if self.brackets != 0:
            raise Syntaxfel("Saknad högerparentes vid radslutet ")
        

    def readGroup(self):
        if self.q.peek().isalpha():
            self.readAtom()
            if self.q.peek().isdigit():
                self.readNum()
        elif self.q.peek() == "(":
            self.brackets += 1
            self.q.dequeue()
            while self.q.peek() != "." and self.q.peek() != ")":
                self.readMolekyl()
        elif self.q.peek() == ")" and self.brackets != 0:
            self.brackets -= 1
            self.q.dequeue()
            if self.q.peek().isdigit():
                self.readNum()
            else:
                raise Syntaxfel("Saknad siffra vid radslutet ")
        else:
            raise Syntaxfel("Felaktig gruppstart vid radslutet ")


    def readAtom(self):
        atom = self.readLETTER()
        if self.q.peek().isdigit() and self.isAtom(atom):
            return
        elif self.q.peek().islower():
            atom += self.readLetter()
            if self.isAtom(atom):
                return
            else:
                raise Syntaxfel("Okänd atom vid radslutet ")
        elif self.isAtom(atom):
            return
        else:
            raise Syntaxfel("Okänd atom vid radslutet ")


    def readLETTER(self):
        letter = self.q.dequeue()
        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if letter in letters:
            return(letter)
        raise Syntaxfel("Saknad stor bokstav vid radslutet " + letter)


    def readLetter(self):
        # We dont raise any errors for this, because an atom might only contain a second letter
        letters = "abcdefghijklmnopqrstuvwxyz"
        if self.q.peek() in letters:
            lettter = self.q.dequeue()
            return(lettter)
        return


    def readNum(self):
        number = int(self.q.dequeue())
        if number == 0:
            raise Syntaxfel("För litet tal vid radslutet ")
        while self.q.peek().isdigit():
            number = number * 10 + int(self.q.dequeue())
        if number > 1:
            return
        elif number < 2:
            raise Syntaxfel("För litet tal vid radslutet ")


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
        return result
    except Syntaxfel as fel:
        kvar = ""
        while not formel.q.isEmpty():
            char = formel.q.dequeue()
            if char != ".":
                kvar += char
        return str(fel) + kvar


def main():
    molekyl = input()
    while not molekyl == "#":
        resultat = kollaMolekyl(molekyl)
        print(resultat)
        molekyl = input()


if __name__ == "__main__":
    main()