"""
Felix Larsson
Labbpartner: Anton Kancans
DD1320 Tillämpad datalogi
Labb 2
2024-09-06
"""

from array import array

class ArrayQ():
    def __init__(self):
        self.__my_array = array('i')

    def __str__(self):
        return str(self.__my_array)

    def is_empty(self):
        return len(self.__my_array) == 0

    def size(self):
        return len(self.__my_array)

    def enqueue(self, item):
        self.__my_array.append(item)

    def dequeue(self):
        return self.__my_array.pop(0)


if __name__ == "__main__":
    q = ArrayQ()
    q.enqueue(1)
    q.enqueue(2)
    x = q.dequeue()
    y = q.dequeue()
    if (x == 1 and y == 2):
        print("OK")
    else:
        print("FAILED")