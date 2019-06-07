import math

def merge(arr1, arr2):
    result = []
    i = 0
    j = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1
    while i < len(arr1):
        result.append(arr1[i])
        i += 1
    while j < len(arr2):
        result.append(arr2[j])
        j += 1
    return result

def merge_sort(arr):
    if len(arr) <= 1: return arr
    mid = int(math.floor(len(arr) // 2))
    lower = merge_sort(arr[:mid])
    upper = merge_sort(arr[mid:])
    return merge(lower, upper)

