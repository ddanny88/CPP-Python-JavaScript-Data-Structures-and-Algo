// Binary Search written in C++
#include <iostream>
#include <cmath>
#include <vector>
using namespace std;


int binary_search(vector<int> arr, int key) {
    int lower {0};
    int upper = arr.size() - 1;
    int mid = floor((lower + upper)/2);
    bool found {false};
    while (lower <= upper and !found) {
        if (key == arr[mid]) {
            found = true;
            return mid;
        } else if (key < arr[mid]) {
            upper = mid - 1;
        } else {
            lower = mid + 1;
        }
        mid = floor((lower + upper)/2);
    }
    if (!found) return false;
}


int main() {
    vector<int>data{1,2,3,4,5,6,7,8,9,10};
    int key{};
    cout << "Enter key: " << endl;
    cin >> key;

    int pos = binary_search(data, key);
    cout << "key is at position: " << pos << endl;
    return 0;
}