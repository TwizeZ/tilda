from linkedQFile import LinkedQ
from molgrafik import *
from hashtest import *

class Syntaxfel(Exception):
    pass


class Ruta:
    def __init__(self, atom="( )", num=1):
        self.atom = atom
        self.num = num
        self.next = None
        self.down = None


def readformel(q):
    if not q.isEmpty():
        formel = readMolekyl(q)

        if not q.isEmpty() and q.peek() == ")":  # Om den upptäcker en högerparantes här så har det inte öppnats en vänsterparantes innan
            raise Syntaxfel("Felaktig gruppstart")

        return formel

def readMolekyl(q):
    if not q.isEmpty():
        mol = readGroup(q)

        if not q.isEmpty() and q.peek() == ")":
            return mol # Om den returnar till Group - OK, om den returnar till formel - inte OK

        if not q.isEmpty():
            mol.next = readMolekyl(q)

        return mol

def readGroup(q):
    if not q.isEmpty():

        rutan = Ruta()

        if q.peek() == "(":  # Öppnar högerparantes och ser till att den stängs igen
            q.dequeue()
            rutan.down = readMolekyl(q)


            if q.isEmpty() or not q.peek() == ")":  # Om parantesen inte stängs
                raise Syntaxfel("Saknad högerparentes")

            else:
                q.dequeue()
                rutan.atom = "( )"

                if not q.isEmpty() and q.peek() in "0123456789":
                    rutan.num = readNum(q)

                else:   # Om det inte finns en siffra efter parantesen
                    raise Syntaxfel("Saknad siffra")

        elif q.peek().upper() in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":  # Om det är en bokstav
            rutan.atom = readAtom(q)

            if not q.isEmpty() and q.peek() in "0123456789":
                rutan.num = readNum(q)

        else:   # Om det inte är en parantes eller bokstav så är det fel
            raise Syntaxfel("Felaktig gruppstart")

        return rutan

def readAtom(q):
    if not q.isEmpty():
        atom = readLETTER(q)

        if not q.isEmpty() and q.peek() in "abcdefghijklmnopqrstuvwxyz":
            atom += readletter(q)


        return atom

def readLETTER(q):
    if not q.isEmpty():
        letter = q.peek()

        if letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":  # Om det är en stor bokstav
            q.dequeue()
            atom = letter
            next = False

            # Foljande kollar om det är en giltig atom
            if not q.isEmpty() and q.peek() in "abcdefghijklmnopqrstuvwxyz":
                next = True
                atom += q.peek()

            if not inAtomList(atom):
                if next is True:
                    q.dequeue()
                raise Syntaxfel("Okänd atom")

        else:
            raise Syntaxfel("Saknad stor bokstav")

        return letter

def readletter(q):
    if not q.isEmpty():
        letter = q.dequeue()
        return letter

def readNum(q):
    if not q.isEmpty():
        num = q.dequeue()

        if num == "0":
            raise Syntaxfel("För litet tal")

        elif num == "1":

            if q.isEmpty() or q.peek() not in "0123456789": # Om det inte finns en till siffra efter 1an
                raise Syntaxfel("För litet tal")

        # Följande dequeue:ar resterande siffror
        number = True
        while number:
            if not q.isEmpty() and q.peek() in "0123456789":
                num += q.dequeue()

            else:
                number = False

        return int(num)

def inAtomList(atom):
    # Funktion för att kolla om atomen är korrekt
    atoms = "H   He  Li  Be  B   C   N   O   F   Ne  Na  Mg  Al  Si  P   S   Cl  Ar  K   Ca  Sc  Ti  V   Cr Mn  Fe  Co  Ni  Cu  Zn  Ga  Ge  As  Se  Br  Kr  Rb  Sr  Y   Zr  Nb  Mo  Tc  Ru  Rh  Pd  Ag  Cd  In  Sn  Sb  Te  I   Xe  Cs  Ba  La  Ce  Pr  Nd  Pm  Sm  Eu  Gd  Tb  Dy  Ho  Er  Tm  Yb  Lu  Hf  Ta  W   Re  Os  Ir  Pt  Au  Hg  Tl  Pb  Bi  Po  At  Rn  Fr  Ra  Ac  Th  Pa  U   Np  Pu  Am  Cm  Bk  Cf  Es  Fm  Md  No  Lr  Rf  Db  Sg  Bh  Hs  Mt  Ds  Rg  Cn  Fl  Lv"
    atomlist = atoms.split()
    if atom in atomlist:
        return True
    else:
        return False

def checkSyntax(formel):
    """ Används endast för unittest"""
    q = LinkedQ()
    for char in formel:
        q.enqueue(char)
    try:
        readformel(q)
        return "Formeln är syntaktiskt korrekt"
    except Syntaxfel as felet:
        rest = str(q).strip()
        result = str(felet) + " vid radslutet " + rest
        return result

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




def main():
    rad = input()
    while rad[0] != "#":
        q = LinkedQ()
        for tkn in rad:
            q.enqueue(tkn)
        try:
            mol = readformel(q)
            print("Formeln är syntaktiskt korrekt")

            mg = Molgrafik()
            mg.show(mol)

            print(weight(mol))
        except Syntaxfel as felet:
            rest = str(q).strip()
            print(felet, "vid radslutet", rest)

        rad = input()




main()
