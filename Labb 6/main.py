import timeit


class Song:
    def __init__(self, track_id, song_id, artist_name, song_title):
        self.track_id = track_id
        self.song_id = song_id
        self.artist_name = artist_name
        self.song_title = song_title

    def __str__(self):
        return f"{self.track_id} {self.song_id} - {self.artist_name}, {self.song_title}"
    
    def __lt__(self, other):
        return self.artist_name < other.artist_name


def readfile(filename):
    songs_list = []
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            track_id, song_id, artist_name, song_title = line.strip().split("<SEP>")
            song = Song(track_id, song_id, artist_name, song_title)
            songs_list.append(song)
    songs_list.sort()

    return songs_list



def linear_search(songs, artist):                   # tidskomplexitet O(n)
    for song in songs:
        if song.artist_name == artist:
            return song
    return None


def binary_search(arr, target):                     # tidskomplexitet O(log n)
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return target[mid]
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return None


def hash_search(songs, artist):                     # tidskomplexitet O(1)
    if artist in songs:
        return songs[artist]
    else:
        return None


def main():
    unique_file = "unique_tracks.txt"
    # unique_file = "unique_eighth.txt"

    songs_list = readfile(unique_file)

    for song in songs_list:
        print(song)
    print("No. of tracks:", len(songs_list))
    print()

    # songs_list = songs_list[:500000]            # Kortar ner listan för att kunna mäta tider

    test_artist1 = songs_list[-1].artist_name
    test_artist2 = songs_list[-1]
    
    linear_time = timeit.timeit(stmt = lambda: linear_search(songs_list, test_artist1), number = 10000)
    print("Linjär tid:", round(linear_time, 5))

    binary_time = timeit.timeit(stmt = lambda: binary_search(songs_list, test_artist2), number = 10000)
    print("Binär tid:", round(binary_time, 5))

    hash_dict = {}
    for song in songs_list:
        hash_dict[song.song_title] = song.song_id

    hash_time = timeit.timeit(stmt = lambda: hash_search(hash_dict, test_artist1), number = 10000)
    print("Hash tid:", round(hash_time, 5))


if __name__ == "__main__":
    main()