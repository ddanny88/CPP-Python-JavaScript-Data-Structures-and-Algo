# Binary Searching algorithm written in Python.

def binary_search(items, key):
    upper = len(items) - 1
    lower = 0
    mid = round((upper + lower)//2)
    found = False

    while lower <= upper and not found:
        if key == items[mid]:
            found = True
            return f'{items[mid]} is at position {mid}.'
        elif key < items[mid]:
            upper = mid - 1
        else:
            lower = mid + 1
        mid = round((upper + lower)//2)
    if not found: return None

