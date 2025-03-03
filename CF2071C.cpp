#include <iostream>
#include <vector>
using namespace std;
#define N 100010
vector<int> graph[N];
void dfs(int x, int p)
{
    for(int &e: graph[x])
    {
        if (e!=p)
        {
            dfs(e, x);
        }
    }
    cout<<x<<' ';
}
void solve()
{
    int n,s,e;
    cin>>n>>s>>e;
    for(int i=0;i<n-1;i++)
    {
        int u,v;
        cin>>u>>v;
        graph[u].push_back(v);
        graph[v].push_back(u);
    }

    dfs(e, -1);
    cout<<endl;
    for(int i=1;i<=n;i++)
    {
        graph[i].clear();
    }
}
int main()
{
    int t;
    cin>>t;
    for(int i=0;i<t;i++)
    {
        solve();
    }
    return 0;
}
