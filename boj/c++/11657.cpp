#include <iostream>
#include <climits>
#define fastio ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
using namespace std;
int N, M;
struct e_t{
    int a, b, c;
} E[6001];

long long Visited[501];

int main(){
    fastio

    cin >> N >> M;
    for (int i = 1; i <= N;i++)
        Visited[i] = INT_MAX;
    for (int i = 1; i <= M; i++)
        cin >> E[i].a >> E[i].b >> E[i].c;

    Visited[1] = 0;
    bool isNegativeCycle = false;

    for (int i = 1; i < N; i++){
        for (int j = 1; j <= M; j++){
            if (Visited[E[j].a] != INT_MAX && Visited[E[j].a] + E[j].c < Visited[E[j].b]){
                Visited[E[j].b] = Visited[E[j].a] + E[j].c;
            }
        }
    }

    for (int j = 1; j <= M; j++){
        if (Visited[E[j].a] != INT_MAX && Visited[E[j].a] + E[j].c < Visited[E[j].b]){
            isNegativeCycle = true;
            break;
        }
    }

    if (isNegativeCycle)
        cout << "-1\n";
    else{
        for (int i = 2; i <= N; i++){
            cout << (Visited[i] == INT_MAX ? -1 : Visited[i]) << "\n";
        }
    }

    return 0;
}