#include <iostream>
#include <vector>
using namespace std;

int main() {

    vector<int> data { 5, 1, 3, 2, 4 };
    int temp {};
    for (int i = 1; i < data.size(); i++) {
        for (int j = 0; j < data.size() - i; j++) {
            if (data[j] > data[j + 1]) {
                temp = data[j];
                data[j] = data[j + 1];
                data[j + 1] = temp;
            }
        }
    }
    return 0;
}