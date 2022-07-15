#include <iostream>
#include <algorithm>
using namespace std;
#define fastio ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);

int N;
struct arr_t{
    int value;
    int prev_index;
    inline bool operator==(const arr_t & ref) const {
        return this->value < ref.value;
    }
};

arr_t A[1000001], T[1000001];
int T_length;

int main(){
    fastio;

    cin >> N;
    for (int i = 1; i <= N; i++){
        cin >> A[i].value;
    }

    for (int i = 1; i <= N; i++){
        arr_t *idx = lower_bound(T, T + T_length, A[i]);
        *idx = {A[i].value, i};
        A[i].prev_index = idx[-1].prev_index;
    }

    return 0;
}
