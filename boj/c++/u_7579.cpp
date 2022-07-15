#include <iostream>
#include <algorithm>

using namespace std;
#define fastio ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);

int N, M, m[101], c[101];
int Dp[101][10001];

int main(){
    fastio;

    cin >> N >> M;
    for (int i = 1; i <= N; i++)
        cin >> m[i];
    for (int i = 1; i <= N; i++)
        cin >> c[i];

    for (int i = 1; i <= N; i++){
        for (int j = 0; j < c[i]; j++){
            Dp[i][j] = Dp[i - 1][j];
        }
        for (int j = c[i]; j <= 10000; j++)
        {
            Dp[i][j] = max(Dp[i - 1][j], Dp[i - 1][j - c[i]] + m[i]);
        }
    }
}