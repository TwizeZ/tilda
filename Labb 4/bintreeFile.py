"""
Felix Larsson
Labbpartner: Anton Kancans
DD1320 Tillämpad datalogi
Labb 2
2024-09-06
"""

class Node:                                                 # Skapar en nod
    def __init__(self, value):                              # Nodens konstruktor
        self.value = value
        self.left = None
        self.right = None


class Bintree:                                              # Skapar ett träd
    def __init__(self):                                     # Trädets konstruktor
        self.root = None

    def __contains__(self, value):                          # Kollar om ett värde finns i trädet
        return finns(self.root, value)
    
    def put(self, new_value):                               # Lägger till ett värde i trädet
        self.root = putta(self.root, new_value)

    def write(self):                                        # Skriver ut trädet
        skriv(self.root)
        print("\n")


def putta(p, new_value):
    if p is None:                                           # Om trädet är tomt blir new_value roten
        return Node(new_value)
    elif new_value < p.value:                               # Om new_value är mindre än roten går vi till vänster
        p.left = putta(p.left, new_value)                   # Anropar sig själv rekursivt
    elif new_value > p.value:                               # Om new_value är större än roten går vi till höger
        p.right = putta(p.right, new_value)                 # Anropar sig själv rekursivt
    return p                                                # Returnerar roten


def finns(p, value):
    if p is None:                                           # Om trädet är tomt finns inga values
        return False
    elif value == p.value:                                  # Om value är roten returneras True
        return True
    elif value < p.value:                                   # Om value är mindre än roten går vi till vänster
        return finns(p.left, value)                         # Anropar sig själv rekursivt
    elif value > p.value:                                   # Om value är större än roten går vi till höger
        return finns(p.right, value)                        # Anropar sig själv rekursivt


def skriv(p):
    if p is not None:                                       # Om trädet inte är tomt skrivs det ut
        skriv(p.left)                                       # Skriver ut till vänster om roten
        print(p.value)                                      # Skriver ut roten
        skriv(p.right)                                      # Skriver ut till höger om roten
