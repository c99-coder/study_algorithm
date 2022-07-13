#include <iostream>

using namespace std;

int N, M, a, b, c;

int U[1000001];

int grp(int a){
    if (U[a] == a)
        return a;
    return U[a] = grp(U[a]);
}

void join(int a, int b){
    int aRoot = grp(a), bRoot = grp(b);
    U[bRoot] = aRoot;
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> N >> M;
    for (int i = 0; i <= N; i++) {
        U[i] = i;
    }
    for (int i = 0; i < M; i++) {
        cin >> c >> a >> b;
        if (c == 0){
            join(a, b);
        }
        else {
            if (grp(a) == grp(b))
                cout << "YES\n";
            else
                cout << "NO\n";
        }
    }
}