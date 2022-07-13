#include <iostream>
using namespace std;

int gcd(int x, int y){
	return y ? gcd(y, x%y) : x;
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    pair<int, int> p[3];
    cin >> p[0].first >> p[0].second >> p[1].first >> p[1].second;
    p[2].first = p[0].first * p[1].second + p[1].first * p[0].second;
    p[2].second = p[0].second * p[1].second;
    int min = gcd(p[2].first, p[2].second);
    cout << p[2].first/min << " " << p[2].second/min;
}