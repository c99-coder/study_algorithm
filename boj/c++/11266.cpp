#include <iostream>
#include <vector>

using namespace std;

int V, E, a, b;
vector<int> AL[10001];

int VisitOrder[10001];
int CutVertex[10001];

int Answer[10001], sAns=0;

int order=0;
int dfs(int curr, int parent){
    VisitOrder[curr] = ++order;

    int minOrder = VisitOrder[curr];

    int child = 0;
    for (int next : AL[curr]){
        if (next == parent)
            continue;
        if (VisitOrder[next] > 0){
            minOrder = VisitOrder[next] < minOrder ? VisitOrder[next] : minOrder;
        }
        else{
            child++;
            int low = dfs(next, curr);

            if (parent && VisitOrder[curr] <= low)
                CutVertex[curr] = 1;
            minOrder = low < minOrder ? low : minOrder;
        }
    }
    if(!parent && child >= 2){
        CutVertex[curr] = 1;
    }
    return minOrder;
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> V >> E;
    for (int i = 0; i < E; i++){
        cin >> a >> b;
        AL[a].push_back(b);
        AL[b].push_back(a);
    }

    for (int i = 1; i <= V; i++){
        if (VisitOrder[i] == 0){
            dfs(i, 0);
        }
    }

    for (int i = 1; i <= V; i++){
        if (CutVertex[i])
            Answer[sAns++] = i;
    }
    cout << sAns << "\n";
    for (int i = 0; i < sAns; i++)
        cout << Answer[i] << " ";
    cout << "\n";

    return 0;
}