from linkedQFile import LinkedQ

class Syntaxfel(Exception):  # Skapar egen exception
    pass


def readMolekyl(q):
    readAtom(q)
    if q.peek() == ".":  # Om kön är tom
        q.dequeue()  # avslutar
    else:
        readNum(q)  # Läser siffran

def readAtom(q):
    readLETTER(q)   # Läser stora bokstaven
    if q.peek() == ".":  # Om kön är tom
        return  # Går tillbaka till readMolekyl()
    else:
        readletter(q)   # Läser lilla bokstaven

def readLETTER(q):
    letter = q.dequeue()
    if letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":  # Om det är en stor bokstav
        return
    raise Syntaxfel("Saknad stor bokstav vid radslutet " + letter)

def readletter(q):
    if q.peek() in "abcdefghijklmnopqrstuvwxyz":    # Om det är en liten bokstav
        q.dequeue()
        return
    return

def readNum(q):
    num = int(q.dequeue())
    if num >= 2:    # Om siffran är större än 1 är det ok
        return
    elif num <= 0:  # Om den är mindre eller lika med 0, raise Syntaxfel
        raise Syntaxfel("För litet tal vid radslutet ")
    else:   # Om den ÄR 1
        num2 = q.dequeue()
        if num2 != ".":  # Om det finns mer än en siffra i talet t.ex 11, 15, 16 o.s.v
            return
        else:   # Annars är det bara en 1a, och då raisar vi syntaxfel
            raise Syntaxfel("För litet tal vid radslutet")

def storeMolekyl(molekyl):
    q = LinkedQ()
    for char in molekyl:    # Lägger in varje karaktär i en kö
        q.enqueue(char)
    q.enqueue(".")  # Slut-karaktär
    return q

def checkSyntax(molekyl):
    q = storeMolekyl(molekyl)
    try:
        readMolekyl(q)
        return "Formeln är syntaktiskt korrekt"
    except Syntaxfel as fel:
        kvar = ""
        while not q.isEmpty():  # Sparar alla resterande karaktärer för utskrift
            char = q.dequeue()
            if char != ".":
                kvar += char
        return str(fel) + kvar

def main():
    molekyl = input()
    while not molekyl == "#":
        resultat = checkSyntax(molekyl)
        print(resultat)
        molekyl = input()


if __name__ == '__main__':
    main()
