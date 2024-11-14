"""
Felicia Watz
Labbpartner Tove Lindegren
DD1320 Till�mpad Datalogi
Labb 6: S�kning och sortering
2023-10-06
"""

# Bin�rs�kning - kattis

# S�kning & sortering - ladda ner filen

# Lista med objekt

class Song:
    def __init__(self, track_id, song_id, artist, song_title):
        self.track_id = track_id
        self.song_id = song_id
        self.artist = artist
        self.song_title = song_title

    def __str__(self):
        info = "Song title: " + self.song_title + "\nArtist: " + self.artist + "\n"
        return info

    def __lt__(self, other):
        return self.artist < other.artist

# Modul timeit
"""
1. stmt representerar statement, allts� koden vi vill kolla p�
2. number representerar antalet g�nger koden k�rs
3. timeit tar tid p� hur l�ng tid det tar att k�ra koden
4. utskriften blir ett float-tal (decimaltal)
"""

# Tidtagning - s�kning

# linj�r - osorterad, bin�r - sorterad & s�kning i hashtabell

import timeit

def readfile(filename):
    lista = []

    with open(filename, "r", encoding="utf-8") as file:
        for rad in file:
            sep_rad = rad.split("<SEP>")
            unique_song = Song(sep_rad[0], sep_rad[1], sep_rad[2],
                               sep_rad[3].strip("\n"))  # sparar annars nedhoppet och det s�g wack ut
            lista.append(unique_song)

    return lista


def linsok(lista, testartist):
    for i in range(len(lista)):
        if lista[i].artist == testartist:
            return True
    return False


def binsok(lista, testartist):

    left = 0
    right = len(lista) - 1

    while left <= right:
        mid = (left + right) // 2  # Hitta mitten av listan

        if lista[mid] == testartist:
            return lista[mid]
        elif lista[mid] < testartist:
            left = mid + 1  # S�k i den h�gra halvan
        else:
            right = mid - 1  # S�k i den v�nstra halvan

    return None


def hashsok(my_dict, testartist):
    if testartist in my_dict:
        return my_dict[testartist]
    else:
        return None

def sort_artist(lista):
    list_artists = []
    for i in lista:
        artist = i.artist
        list_artists.append(artist)
    return list_artists


def main():

    #filename = "unique_tracks.txt"
    filename = "unique_half.txt"
    #filename = "unique_quarter.txt"

    lista = readfile(filename)
    mindreLista = lista[0:250000]
    n = len(mindreLista)
    print("Antal element =", n)

    sista1 = mindreLista[n-1]
    testartist = sista1.artist

    linjtid = timeit.timeit(stmt=lambda: linsok(mindreLista, testartist), number=10000)
    print("Linj�rs�kningen tog", round(linjtid, 4), "sekunder")

    lista_sort = sort_artist(mindreLista)
    sista2 = lista_sort[n - 1]
    testartist = sista2

    binsoktid = timeit.timeit(stmt=lambda: binsok(lista_sort, testartist), number=10000)
    print("Bin�rs�kningen tog", round(binsoktid, 4), "sekunder")

    my_dict = {}
    n = 250000
    for count, obj in enumerate(lista):
        my_dict[obj.song_title] = obj.song_id
        if count == n:
            break

    hashtid = timeit.timeit(stmt=lambda: hashsok(my_dict, testartist), number=10000)
    print("Hashs�kningen tog", round(hashtid, 4), "sekunder")


    print(linsok(mindreLista, sista1.artist))           # True
    print(binsok(lista_sort, sista2))                   # None
    print(hashsok(my_dict, sista2))                     # None

main()

