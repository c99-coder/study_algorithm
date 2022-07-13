#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;
int n,m;
int d[55][55];
bool visited[55][55];
int dx[4] = {0,0,-1,1}; 
int dy[4] = {1,-1,0,0};
char map[55][55];

bool inner(int x,int y){
    return (0<=x && x<n && 0<=y && y<m);
}

int solve(int x,int y) {
    if(visited[x][y]) return 1e9;
    int&ret = d[x][y];
    if(ret != -1) return ret;
    ret=0;
    
    visited[x][y]= 1;
    int c = map[x][y]-'0';
    for(int i=0;i<4;i++){
        int nx = x+dx[i]*c;
        int ny = y+dy[i]*c;
        if(inner(nx,ny) && map[nx][ny] != 'H') {
            ret = max(ret,solve(nx,ny)+1);
        }
    }
    visited[x][y]=0;
    return ret;
}

int main(){
    memset(d,-1,sizeof(d));
    scanf(" %d %d",&n,&m);
    for(int i=0;i<n;i++){
        for(int j=0;j<m;j++){
            scanf(" %1c",&map[i][j]);
        }
    }
    int ans = solve(0,0);
    printf("%d\n",(ans>=1e9) ? -1 : ans+1);
}
