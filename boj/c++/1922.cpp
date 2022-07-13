#include <iostream>
#include <algorithm>

using namespace std;

int N, M;

struct e_t{
    int a, b, c;
    bool operator < (const e_t &ref) const{
        return this->c < ref.c;
    }
} Edge[100000];

int U[1001];
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
    for (int i = 0; i < M; i++){
        cin >> Edge[i].a >> Edge[i].b >> Edge[i].c;
    }

    sort(Edge, Edge+M);

    for (int i = 1; i <= N; i++){
        U[i] = i;
    }
    int Answer = 0;
    for (int i = 0; i < M; i++){
        if (grp(Edge[i].a) != grp(Edge[i].b)){
            join(Edge[i].a, Edge[i].b);
            Answer += Edge[i].c;
        }
    }
    cout << Answer << "\n";
}