#include <iostream>
#define fastio ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
using namespace std;

const int INF = 1e8;

int N, M;
int AM[101][101];

int main(){
    fastio
    cin >> N >> M;
    for (int i=1; i <= N; i++){
        for (int j=1; j <= N; j++){
            if (i!=j)
                AM[i][j] = INF;
        }
    }

    int a, b, c;
    for (int i=1; i <=M; i++){
        cin >> a >> b >> c;
        AM[a][b] = c < AM[a][b] ? c : AM[a][b];
    }

    for (int k = 1; k <= N; k++){
        for (int i = 1; i <= N; i++){
            for (int j = 1; j <= N; j++){
                if (AM[i][j] > AM[i][k] + AM[k][j])
                    AM[i][j] = AM[i][k] + AM[k][j];
            }
        }
    }
    for (int i = 1; i <= N; i++){
        for (int j = 1; j <= N; j++){
            cout << (AM[i][j] == INF ? 0 : AM[i][j]) << ' ';
        }
        cout << "\n";
    }
    return 0;
}