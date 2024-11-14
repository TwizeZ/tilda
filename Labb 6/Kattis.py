
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return target
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return None


def main():
    #Läs in listan
    indata = input().strip()
    the_list = indata.split()
    #Läs in nycklar att söka efter
    key = input().strip()
    while key != "#":
        print(binary_search(the_list, key))
        key = input().strip()

main()