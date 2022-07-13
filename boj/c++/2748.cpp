#include <iostream>

using namespace std;

long long fib[91] = {0,1,};
int n;

int main(){
    scanf("%d",&n);
    for (int i = 2; i <= n; i++)
        fib[i] = fib[i - 1] + fib[i - 2];
    printf("%lld", fib[n]);
}