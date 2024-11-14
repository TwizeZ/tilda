"""
Felicia Watz
Labbpartner Tove Lindegren
DD1320 Tillämpad Datalogi
Labb 4: Grafer, breddenförstsökning del 1
2023-09-22
"""

# Andra versionen
from bintreeFile import Bintree
from linkedQFile import LinkedQ

# svenska trädet från lab 3, tagit bort print delen endast
svenska = Bintree()
with open("word3.txt", "r", encoding="utf-8") as svenskfil:
    for rad in svenskfil:
        ordet = rad.strip()
        if ordet in svenska:
            pass
        else:
            svenska.put(ordet)

gamla = Bintree()


def makechildren(startord, slutord, q):
    gamla.put(startord)  # lägger in startordet i gamla-trädet

    for i in range(len(startord)):
        alfabet = "abcdefghijklmnopqrstuvwxyzåäö"
        for bokstav in alfabet:  # byter ut bokstäverna på de olika ställerna
            if i == 0:
                nytt_ord = bokstav + startord[1] + startord[2]
            elif i == 1:
                nytt_ord = startord[0] + bokstav + startord[2]
            elif i == 2:
                nytt_ord = startord[0] + startord[1] + bokstav

            if nytt_ord in svenska:
                if nytt_ord not in gamla:  # checkar så att ordet existerar och inte är ett dumbarn
                    if nytt_ord == slutord:  # om ordet är det sökta slutordet så returnerar den True
                        return True
                    else:
                        q.enqueue(nytt_ord)  # annars lägger till i kön och lägger till i dumbarns-trädet
                        gamla.put(nytt_ord)


def main():
    q = LinkedQ()
    startord = input("Skriv ett ord med tre bokstäver: ")
    q.enqueue(startord)  # köar först ordet
    slutord = input("Skriv ett slutord med tre bokstäver: ")
    makechildren(startord, slutord, q)  # skickar in startordet, slutordet och kön
    while not q.isEmpty():  # så länge det finns något i kön
        word = q.dequeue()
        if makechildren(word, slutord, q) is True:  # när den har kommit fram till slutordet
            print("Det finns en väg till slutordet " + slutord)
            break
        elif q.isEmpty() is True:  # om den har gått igenom och tömt hela kön men ej hittat slutordet
            print("Det finns ingen väg till slutordet " + slutord)
            break


main()
