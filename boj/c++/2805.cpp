#include <iostream>
#define MAX 2000000000

using namespace std;

int trees[1000000];
int n, m, mid;
int answer;

int main(){
    scanf("%d %d", &n, &m);
    for (int i = 0; i <n; i++){
        scanf("%d", &trees[i]);
    }

    int start = 1, end = MAX;
    while (start <= end){
        mid = (start + end) / 2;
        long long int total = 0;
        for (int i = 0; i < n; i++)
            if (trees[i] > mid)
                total += trees[i] - mid;

        if (total < m)
            end = mid - 1;
        else{
            answer = mid;
            start = mid + 1;
        }
    }
    printf("%d", answer);
}