#include <iostream>
#include <vector>
#include <queue>

#define fastio ios_base::sync_with_stdio(0); cin.tie(); cout.tie();
#define INF 2000000000

using namespace std;

int V, E, Start;
struct e_t{
    int node;
    int cost;
    bool operator < (const e_t &ref) const {
        return this->cost > ref.cost;
    }
};

vector<e_t> AL[20001];

int Visited[20001];

int main(){
    fastio
    cin >> V >> E;
    cin >> Start;
    int a, b, c;
    for (int i = 0; i < E; i++){
        cin >> a >> b >> c;
        AL[a].push_back({b, c});
    }

    for (int i = 1; i <= V; i++)
        Visited[i] = INF;

        priority_queue<e_t> PQ;
    Visited[Start] = 0;
    PQ.push({Start, 0});

    while (!PQ.empty()){
        e_t curr = PQ.top();
        PQ.pop();
        for (e_t next : AL[curr.node]){
            int cost = curr.cost + next.cost;
            if (cost < Visited[next.node]){
                Visited[next.node] = cost;
                PQ.push({next.node, cost});
            }
        }
    }
    for (int i = 1; i <= V; i++){
        if (Visited[i] == INF)
            cout << "INF\n";
        else
            cout << Visited[i] << "\n";
    }
    return 0;
}