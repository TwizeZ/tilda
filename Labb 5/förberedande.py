lista = [1, 2, 3, 4, 5]

def utskrift1(lista):
    if len(lista) > 0:
        print(lista[0])
        utskrift1(lista[1:])

def utskrift2(lista):
    if len(lista) > 0:
        utskrift2(lista[1:])
        print(lista[0])

utskrift1(lista)                # Skriver ut 1 2 3 4 5
utskrift2(lista)                # Skriver ut 5 4 3 2 1