"""
Felicia Watz
Labbpartner: Tove Lindegren
DD1320 Tillämpad Datalogi
Labb 10: Molekylvikter
2023-11-18
"""

#  from Lab9draft import *
from molgrafik import *

from linkedQFile import LinkedQ
from molgrafik import *

class Ruta:
    def __init__(self, atom="( )", num=1):
        self.atom = atom
        self.num = num
        self.next = None
        self.down = None


class Syntaxfel(Exception):
    pass

def readFormel(molekyl):
    q = storeChem(molekyl)

    try:
        formel = readMol(q)
        return formel
    except Syntaxfel as fel:
        rest1 = str(q).strip()
        rest = rest1.strip(".")
        print(str(fel) + " " + rest)


def readMol(q):
    mol = readGroup(q)
    if q.peek() != "." and q.peek() == ")":
        return mol
    if q.peek() != ".":
        mol.next = readMol(q)
    return mol


def readGroup(q):
    rutan = Ruta()
    if q.peek().isalpha():
        rutan.atom = readAtom(q)
        if q.peek().isdigit():
            rutan.num = readNum(q)
    elif q.peek() == "(":
        q.dequeue()
        if q.peek() != "." and q.peek() != ")":
            rutan.down = readMol(q)
        if q.peek() == ")":
            q.dequeue()
            if not q.peek().isdigit():
                raise Syntaxfel("Saknad siffra vid radslutet")
            rutan.num = readNum(q)
            return rutan
        else:
            raise Syntaxfel("Saknad högerparentes vid radslutet")
    else:
        raise Syntaxfel("Felaktig gruppstart vid radslutet")
    return rutan


def readAtom(q):
    if q.peek().isupper():
        atom = q.dequeue()
        if not q.peek() == "." and q.peek().islower():
            atom += q.dequeue()
        if atom in lista_atomer:
            return atom
        raise Syntaxfel("Okänd atom vid radslutet")
    raise Syntaxfel("Saknad stor bokstav vid radslutet")


def readNum(q):
    if q.peek() == ".":
        q.dequeue()
    else:
        number = q.dequeue()
        if int(number) == 1 and not q.peek().isdigit():
            raise Syntaxfel("För litet tal vid radslutet")
        if int(number) >= 1:
            while q.peek().isdigit() and int(q.peek()) >= 0:
                number += q.dequeue()
            if int(number) >= 2:
                return int(number)
            elif q.peek() == ".":
                return
        else:
            raise Syntaxfel("För litet tal vid radslutet")


def printQ(q):
    while not q.isEmpty():
        word = q.dequeue()
        print(word, end=" ")
    print()


def storeChem(molekyl):
    q = LinkedQ()
    for part in molekyl:
        q.enqueue(part)
    q.enqueue(".")
    return q


atomer = "H   He  Li  Be  B   C   N   O   F   Ne  Na  Mg  Al  Si  P   S   Cl  Ar  K   Ca  Sc  Ti  V   Cr" \
         "Mn  Fe  Co  Ni  Cu  Zn  Ga  Ge  As  Se  Br  Kr  Rb  Sr  Y   Zr  Nb  Mo  Tc  Ru  Rh  Pd  Ag  Cd" \
         "In  Sn  Sb  Te  I   Xe  Cs  Ba  La  Ce  Pr  Nd  Pm  Sm  Eu  Gd  Tb  Dy  Ho  Er  Tm  Yb  Lu  Hf" \
         "Ta  W   Re  Os  Ir  Pt  Au  Hg  Tl  Pb  Bi  Po  At  Rn  Fr  Ra  Ac  Th  Pa  U   Np  Pu  Am  Cm" \
         "Bk  Cf  Es  Fm  Md  No  Lr  Rf  Db  Sg  Bh  Hs  Mt  Ds  Rg  Cn  Fl  Lv"

lista_atomer = atomer.split( )

atom_weight = {
    'H': 1.00794, 'He': 4.002602, 'Li': 6.941, 'Be': 9.012182, 'B': 10.811, 'C': 12.0107, 'N': 14.0067,
    'O': 15.9994, 'F': 18.9984032, 'Ne': 20.1797, 'Na': 22.98976928, 'Mg': 24.3050, 'Al': 26.9815386,
    'Si': 28.0855, 'P': 30.973762, 'S': 32.065, 'Cl': 35.453, 'K': 39.0983, 'Ar': 39.948, 'Ca': 40.078,
    'Sc': 44.955912, 'Ti': 47.867, 'V': 50.9415, 'Cr': 51.9961, 'Mn': 54.938045, 'Fe': 55.845, 'Ni': 58.6934,
    'Co': 58.933195, 'Cu': 63.546, 'Zn': 65.38, 'Ga': 69.723, 'Ge': 72.64, 'As': 74.92160, 'Se': 78.96,
    'Br': 79.904, 'Kr': 83.798, 'Rb': 85.4678, 'Sr': 87.62, 'Y': 88.90585, 'Zr': 91.224, 'Nb': 92.90638,
    'Mo': 95.96, 'Tc': 98, 'Ru': 101.07, 'Rh': 102.90550, 'Pd': 106.42, 'Ag': 107.8682, 'Cd': 112.411,
    'In': 114.818, 'Sn': 118.710, 'Sb': 121.760, 'I': 126.90447, 'Te': 127.60, 'Xe': 131.293, 'Cs': 132.9054519,
    'Ba': 137.327, 'La': 138.90547, 'Ce': 140.116, 'Pr': 140.90765, 'Nd': 144.242, 'Pm': 145, 'Sm': 150.36,
    'Eu': 151.964, 'Gd': 157.25, 'Tb': 158.92535, 'Dy': 162.500, 'Ho': 164.93032, 'Er': 167.259, 'Tm': 168.93421,
    'Yb': 173.054, 'Lu': 174.9668, 'Hf': 178.49, 'Ta': 180.94788, 'W': 183.84, 'Re': 186.207, 'Os': 190.23,
    'Ir': 192.217, 'Pt': 195.084, 'Au': 196.966569, 'Hg': 200.59, 'Tl': 204.3833, 'Pb': 207.2, 'Bi': 208.98040,
    'Po': 209, 'At': 210, 'Rn': 222, 'Fr': 223, 'Ra': 226, 'Ac': 227, 'Pa': 231.03588, 'Th': 232.03806,
    'Np': 237, 'U': 238.02891, 'Am': 243, 'Pu': 244, 'Cm': 247, 'Bk': 247, 'Cf': 251, 'Es': 252, 'Fm': 257,
    'Md': 258, 'No': 259, 'Lr': 262, 'Rf': 265, 'Db': 268, 'Hs': 270, 'Sg': 271, 'Bh': 272, 'Mt': 276,
    'Rg': 280, 'Ds': 281, 'Cn': 285
}

def molecule_weight(molecule):
    total_weight = 0.0

    if molecule.atom == "( )":
        total_weight += molecule_weight(molecule.down) * molecule.num
    else:
        total_weight += atom_weight[molecule.atom] * molecule.num
    if molecule.next:
        total_weight += molecule_weight(molecule.next)
    return total_weight


"""def main():
    while True:
        molekyl = input("")
        if molekyl == "#":
            break

        mol = readFormel(molekyl)
        weight = molecule_weight(mol)
        print("Molekylens vikt är: " + str(weight) + " g/mol")
        mg = Molgrafik()
        mg.show(mol)"""

def main():
    while True:
        molekyl = input("")
        if molekyl == "#":
            break

        try:
            mol = readFormel(molekyl)
            if mol is not None:
                weight = molecule_weight(mol)
                print("Molekylens vikt är: " + str(weight) + " g/mol")
                mg = Molgrafik()
                mg.show(mol)
        except Syntaxfel as fel:
            print("Syntaxfel: " + str(fel))

main()
