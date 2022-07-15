#include <iostream>
#include <climits>
#include <algorithm>
using namespace std;
#define fastio ios_base::sync_with_stdio(0); cin.tie(0);

int N, Row[501], Col[501];
int Dp[501][501];

int main(){
    cin >> N;
    for (int i = 1; i <= N; i++)
        cin >> Row[i] >> Col[i];

    for (int step = 1; step < N; step++){
        for (int start = 1; start + step <= N; start++){
            Dp[start][start + step] = INT_MAX;
            for (int mid = start; mid < start + step; mid++){
                Dp[start][start + step] = min(Dp[start][start + step], Dp[start][mid] + Dp[mid + 1][start + step] + Row[start] * Col[start + step] * Col[mid]);
            }
        }
    }
    
    cout << Dp[1][N] << "\n";
    return 0;
}