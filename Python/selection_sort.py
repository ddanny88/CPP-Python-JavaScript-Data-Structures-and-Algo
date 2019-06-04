# Selection sort written in Python:

data = [ 10, 3, 6, 9, 8, 5, 2, 1, 4, 7 ]

def selection_sort(arr):
    for i in range(len(arr)):
        low = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[low]:
                low = j
        temp = arr[i]
        arr[i] = arr[low]
        arr[low] = temp
    return arr
