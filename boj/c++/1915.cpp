#include <iostream>
#include <algorithm>
using namespace std;

#define fastio ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0)

int N, M, ans;
char c;
int map[1001][1001];
int dp[1001][1001];

int main(){
    fastio;
    cin >> N >> M;

    for (int i = 1; i <= N; i++){
        for (int j = 1; j <= M; j++){
            cin >> c;
            map[i][j] = c - '0';

            if (i == 1 || j == 1)
                dp[i][j] = map[i][j];

            ans = max(ans, dp[i][j]);
        }
    }

    for (int i = 2; i <= N; i++){
        for (int j = 2; j <= M; j++){
            if (map[i][j]){
                dp[i][j] = min(min(dp[i][j-1], dp[i-1][j]), dp[i-1][j-1]) + 1;
            }
            else{
                dp[i][j] = 0;
            }
            ans = max(ans, dp[i][j]);
        }
    }

    cout << ans*ans << "\n";

    return 0;
}