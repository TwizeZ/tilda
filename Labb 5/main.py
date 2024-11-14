from bintreeFile import Bintree
from linkedQFile import LinkedQ

svenska = Bintree()                         # Skapa ett svenska-träd
gamla = Bintree()                           # Skapa ett gamla-träd


class ParentNode:
    def __init__(self, word, parent = None):
        self.word = word
        self.parent = parent

    def writechain(self):
        if self.parent:
            self.parent.writechain()
            print(self.parent.word, "-->", self.word)


class SolutionFound(Exception):
    pass


def makechildren(start_node, end_word, queue):
    alfabet = "abcdefghijklmnopqrstuvwxyzåäö"                               # Alfabetet
    
    for i in range(len(start_node.word)):                                        # Loopar igenom startordet
        for letter in alfabet:                                              # Loopar igenom alfabetet
            if letter in start_node.word:                                        # Om bokstaven redan finns i ordet
                continue                                                    # Fortsätt till nästa bokstav
            else:
                new_word = start_node.word[:i] + letter + start_node.word[i + 1:]               # Byt ut bokstaven
                new_word_node = ParentNode(new_word, start_node)                      # Skapa en nod med det nya ordet
                if new_word in svenska and new_word not in gamla:                     # Om ordet finns i svenska och inte i gamla
                    if new_word == end_word:                                          # Om ordet är slutordet
                        new_word_node.writechain()                                    # Skriv ut vägen
                        return True
                    else:
                        queue.enqueue(new_word_node)
                        gamla.put(new_word)


def main():
    start_word = input("Ange startord: ").lower()
    end_word = input("Ange slutord: ").lower()

    with open("word3.txt", "r", encoding = "utf-8") as ordlista:            # Öppnar ordlistan
        for rad in ordlista:
            ordet = rad.strip()
            if ordet not in svenska:
                svenska.put(ordet)

    queue = LinkedQ()                                                       # Skapa en kö
    first_node = ParentNode(start_word)                                     # Skapa en nod med startordet
    queue.enqueue(first_node)                                               # Lägger till startordet i kön
    while not queue.isEmpty():                                              # Så länge kön inte är tom
        word = queue.dequeue()                                              # Ta det "första" ordet i kön
        if makechildren(word, end_word, queue):                             # Om det finns en väg
            print("Det finns en väg från", start_word, "till", end_word)
            break
        elif queue.isEmpty():                                               # Om det inte finns en väg
            print("Det finns ingen väg från", start_word, "till", end_word)


if __name__ == "__main__":
    main()