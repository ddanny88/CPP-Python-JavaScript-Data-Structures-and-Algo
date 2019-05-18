// Binary Searching alogorithm wrtitten in JavaScript

function binarySearch(arr, key) {
    let upper = arr.length;
    let lower = 0;
    let mid = Math.floor((upper + lower)/2);
    let found = false;

    while (lower <= upper && !found) {
        if (key === arr[mid]) {
            found = true;
            return `${arr[mid]} is at position ${mid}.`
        } else if (key < arr[mid]) {
            upper = mid - 1;
        } else {
            lower = mid + 1;
        }

        mid = Math.floor((upper + lower)/2)
    }
    if (!found) return null;
}

