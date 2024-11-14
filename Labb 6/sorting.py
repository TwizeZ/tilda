import timeit
from main import readfile

def bubble_sort(array_list):          # Från ChatGPT (tidskomplexitet O(n^2))
    n = len(array_list)
    for i in range(n):
        for j in range(0, n-i-1):
            if array_list[j] > array_list[j+1]:
                array_list[j], array_list[j+1] = array_list[j+1], array_list[j]
    return array_list


def quick_sort(array_list):           # Från ChatGPT (tidskomplexitet O(n log n))
    if len(array_list) <= 1:
        return array_list
    pivot = array_list[len(array_list) // 2]
    left = [x for x in array_list if x < pivot]
    middle = [x for x in array_list if x == pivot]
    right = [x for x in array_list if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)
    

def main():
    unique_file = "unique_tracks.txt"

    songs_list = readfile(unique_file)
    # songs_list = songs_list[:100000]                  # Kortar ner listan för att kunna mäta tider

    quick_time = timeit.timeit(stmt=lambda: quick_sort(songs_list), number=1)
    print("Quick sort time:", round(quick_time, 5))

    bubble_time = timeit.timeit(stmt=lambda: bubble_sort(songs_list), number=1)
    print("Bubble sort time:", round(bubble_time, 5))
    


if __name__ == "__main__":
    main()