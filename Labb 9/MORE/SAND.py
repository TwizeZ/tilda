from linkedQFile import LinkedQ

class Syntaxfel(Exception):
    pass

def readformel(q):
    if not q.isEmpty():
        readMolekyl(q)

    if not q.isEmpty() and q.peek() == ")":  # Om den upptäcker en högerparantes här så har det inte öppnats en vänsterparantes innan
        raise Syntaxfel("Felaktig gruppstart")

def readMolekyl(q):
    if not q.isEmpty():
        readGroup(q)

        if not q.isEmpty and q.peek() in "0123456789":
            readNum(q)

        elif not q.isEmpty() and q.peek() == ")":
            return  # Om den returnar till Group - OK, om den returnar till formel - inte OK

        if not q.isEmpty():
            readMolekyl(q)

def readGroup(q):
    if not q.isEmpty():

        if q.peek() == "(":  # Öppnar högerparantes och ser till att den stängs igen
            q.dequeue()
            readMolekyl(q)

            if q.isEmpty() or not q.peek() == ")":  # Om parantesen inte stängs
                raise Syntaxfel("Saknad högerparentes")

            else:
                q.dequeue()

                if not q.isEmpty() and q.peek() in "0123456789":
                    readNum(q)

                else:   # Om det inte finns en siffra efter parantesen
                    raise Syntaxfel("Saknad siffra")

        elif q.peek().upper() in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":  # Om det är en bokstav
            readAtom(q)

            if not q.isEmpty() and q.peek() in "0123456789":
                readNum(q)

        else:   # Om det inte är en parantes eller bokstav så är det fel
            raise Syntaxfel("Felaktig gruppstart")

def readAtom(q):
    if not q.isEmpty():
        readLETTER(q)

        if not q.isEmpty() and q.peek() in "abcdefghijklmnopqrstuvwxyz":
            readletter(q)

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

def readletter(q):
    if not q.isEmpty():
        q.dequeue()

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
                q.dequeue()

            else:
                number = False

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


def main():
    rad = input()
    while rad[0] != "#":
        q = LinkedQ()
        for tkn in rad:
            q.enqueue(tkn)
        try:
            readformel(q)
            print("Formeln är syntaktiskt korrekt")
        except Syntaxfel as felet:
            rest = str(q).strip()
            print(felet, "vid radslutet", rest)
        rad = input()



main()
