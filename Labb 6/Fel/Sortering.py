"""
Felicia Watz
Labbpartner Tove Lindegren
DD1320 Tillämpad Datalogi
Labb 6: Sökning och sortering
2023-10-04
"""

#  Snabbare sortering: Quicksort från föreläsning 8
def quicksort(data):
    sista = len(data) - 1
    qsort(data, 0, sista)


def qsort(data, low, high):
    pivotindex = (low + high) // 2
    # flytta pivot till kanten
    data[pivotindex], data[high] = data[high], data[pivotindex]

    # damerna först med avseende på pivotdata
    pivotmid = partitionera(data, low - 1, high, data[high])

    # flytta tillbaka pivot
    data[pivotmid], data[high] = data[high], data[pivotmid]

    if pivotmid - low > 1:
        qsort(data, low, pivotmid - 1)
    if high - pivotmid > 1:
        qsort(data, pivotmid + 1, high)


def partitionera(data, v, h, pivot):
    while True:
        v = v + 1
        while data[v] < pivot:
            v = v + 1
        h = h - 1
        while h != 0 and data[h] > pivot:
            h = h - 1
        data[v], data[h] = data[h], data[v]
        if v >= h:
            break
    data[v], data[h] = data[h], data[v]
    return v


#  Långsam sortering:
def urvalssortera(data): #  Föreläsning 8, Urvalssortering (Selection sort)
    n = len(data)
    for i in range(n):
        minst = i
        for j in range(i+1,n):
            if data[j] < data[minst]:
                minst = j
        data[minst],data[i] = data[i], data[minst]