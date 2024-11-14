"""
Felix Larsson
Labbpartner: Anton Kancans
DD1320 Tillämpad datalogi
Labb 8
2024-11-01
"""

from linkedQFile import LinkedQ

class Syntaxfel(Exception):
    pass
    

def readMolekyl(q):
    readAtom(q)
    if q.peek() == ".":                                     # Om första i kön är ".", plocka ur kön
        q.dequeue()
    else:                                                   # Annars, readNum()
        readNum(q)
    

def readAtom(q):
    if q.peek().isupper():                                  # Om bokstav 1 är stor, readLETTER()
        readLETTER(q)
        if q.peek().islower():                              # Om bokstav 2 är liten, readLetter()
            readLetter(q)
    else:                                                   # Annars, syntaxfel
        raise Syntaxfel("Syntaxfel: Saknad stor bokstav vid radslutet ")


def readLETTER(q):
    letter = q.dequeue()
    if letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":              # Om första i q är en stor bokstav
        return
    raise Syntaxfel("Saknad stor bokstav vid radslutet " + letter)      # Annars, syntaxfel


def readLetter(q):
    if q.peek() in "abcdefghijklmnopqrstuvwxyz":            # Om första i kön är en liten bokstav
        q.dequeue()                                         # Plockar ut den
        return
    return
    

def readNum(q):
    num1 = int(q.dequeue())                                 # Plockar ut siffran
    if num1 >= 2:                                           # Om siffran är större än 1, return
        return
    elif num1 <= 0:                                         # Om siffran är mindre än 0, raise Syntaxfel
        raise Syntaxfel("För litet tal vid radslut ")
    else:
        num2 = q.dequeue()                             # Om siffran är 1, kolla om det är en siffra till
        if num2 != ".":                                     # Om det är en siffra till, return
            return
        else:                                               # Om det inte är en siffra till, raise Syntaxfel
            raise Syntaxfel("För litet tal vid radslut ")


def storeMolekyl(molekyl):
    q = LinkedQ()                                           # Skapar en kö
    for i in molekyl:                                       # Lägger in varje karaktär i kön
        q.enqueue(i)
    q.enqueue(".")
    return q


def kollaSyntax(molekyl):
    q = storeMolekyl(molekyl)                               # Skapar kö med molekylen
    try:
        readMolekyl(q)                                      # Läser molekylen
        return "Formeln är syntaktiskt korrekt"
    except Syntaxfel as fel:                                # Om det blir syntaxfel
        kvar = ""
        while not q.isEmpty():                              # Sparar resterande karaktärer
            char = q.dequeue()
            if char != ".":                                 # Om det inte är slutet
                kvar += char                                # Lägg till i kvar
        return str(fel) + kvar



def main():
    molekyl = input()
    while not molekyl == "#":                                   # Avbryter om input är "#"
        resultat = kollaSyntax(molekyl)                         # Kollar syntaxen
        print(resultat)                                         # Skriver ut resultatet
        molekyl = input()                                       # Ny input


if __name__ == '__main__':
    main()