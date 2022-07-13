#include <iostream>

using namespace std;

int a[10000];
int n, m;

int main(){
    scanf("%d %d",&n,&m);
    for (int i = 0; i<n; i++) {
        scanf("%d", &a[i]);
    }
    int sum = 0, left = 0;
    int answer = 0;
    for (int right = 0; right<n; right++){
        // printf("%d %d %d\n", left, right, sum);
        sum += a[right];
        while (sum >= m){
            if (sum == m) {
                answer++;
            }
            sum -= a[left];
            left++;
        }
    }
    printf("%d", answer);
}