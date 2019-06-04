# Binary Sorting algorithm written in Python.

def bubble_sort(items):
    temp = None
    for i in range(1, len(items)):
        for j in range(0, len(items) - i):
            if items[j] > items[j + 1]:
                temp = items[j]
                items[j] = items[j + 1]
                items[j + 1] = temp
    return items

