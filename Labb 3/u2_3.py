from bintreeFile import Bintree

svenska = Bintree()                         # Skapa ett träd

with open("word3.txt", "r", encoding = "utf-8") as svenskfil:
    for rad in svenskfil:
        ordet = rad.strip()                 # Ett trebokstavsord per rad
        if ordet in svenska:                # ordet finns redan i sökträdet
            print(ordet, end = " ")
        else:                               # ordet finns inte i trädet
            svenska.put(ordet)              # in i sökträdet

print("\n")

engelska = Bintree()                        # Skapa ett träd

with open("engelska.txt", "r", encoding = "utf-8") as engelskfil:
    for line in engelskfil:
        words = line.strip().split()        # dela upp raden i ord
        for word in words:                  # tar ett ord i taget
            if word in engelska:            # om ordet redan finns i trädet
                pass
            else:                           # om ordet inte finns i trädet
                engelska.put(word)          # lägg in ordet i trädet
                if word in svenska:         # skriver ut ordet om det också finns i svenska trädet
                    print(word, end = " ")