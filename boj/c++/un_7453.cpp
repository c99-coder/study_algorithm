#include<iostream>
#include<algorithm>
#include<vector>

using namespace std;

int N;

int arr[4001][4];
vector<int> A, B;
long long answer = 0;

int main() {

	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	cin >> N;

	for (int i = 0; i < N; i++) 
		for (int j = 0; j < 4; j++) cin >> arr[i][j];


	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			A.push_back(arr[i][0] + arr[j][1]);
			B.push_back(arr[i][2] + arr[j][3]);
		}	
	}

	sort(A.begin(), A.end());
	sort(B.begin(), B.end());
	
    int p1 = 0, p2 = B.size() - 1;
	
    while (p1 < A.size() && p2 >= 0){
        if (A[p1] + B[p2] == 0){
            long long cnt1 = 0;
            int i = p1;
            while
        }
    }

	cout << answer << endl;
	
	return 0;

}