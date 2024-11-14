from bintreeFile import Bintree
from linkedQFile import LinkedQ

svenska = Bintree()                         # Skapa ett svenska-träd
gamla = Bintree()                           # Skapa ett gamla-träd


def makechildren(start_word, end_word, queue):
    alfabet = "abcdefghijklmnopqrstuvwxyzåäö"           # Alfabetet
    
    for i in range(len(start_word)):                    # Loopar igenom startordet
        for letter in alfabet:                          # Loopar igenom alfabetet
            if letter in start_word:                    # Om bokstaven redan finns i ordet
                continue                                # Fortsätt till nästa bokstav
            else:
                new_word = start_word[:i] + letter + start_word[i + 1:]     # Byt ut bokstaven
                if new_word in svenska and new_word not in gamla:           # Om ordet finns i svenska och inte i gamla
                    if new_word == end_word:            # Om ordet är slutordet
                        return True
                    else:
                        queue.enqueue(new_word)
                        gamla.put(new_word)


start_word = input("Ange startord: ").lower()
end_word = input("Ange slutord: ").lower()

with open("word3.txt", "r", encoding = "utf-8") as ordlista:            # Öppnar ordlistan
    for rad in ordlista:
        ordet = rad.strip()
        if ordet not in svenska:
            svenska.put(ordet)

queue = LinkedQ()               # Skapa en kö
queue.enqueue(start_word)       # Lägger till startordet i kön
while not queue.isEmpty():      # Så länge kön inte är tom
    word = queue.dequeue()      # Ta det "första" ordet i kön
    if makechildren(word, end_word, queue):                             # Om det finns en väg
        print("Det finns en väg från", start_word, "till", end_word)
        break
    elif queue.isEmpty():                                               # Om kön är tom
        print("Det finns ingen väg från", start_word, "till", end_word)