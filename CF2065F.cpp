#include <bits/stdc++.h>

using namespace std;
#define N 500010
int arr[N];
int u,v;
vector<int> e[N];
int ans[N];
int n;

bool cmp(int x, int y)
{
    return arr[x]<arr[y];
}
void dfs(int pp, int p, int x)
{
    if (p>=0 && arr[p] == arr[x])
    {
        ans[arr[x]] = 1;
    }
    sort(e[x].begin(), e[x].end(), cmp);

    for(int i=0;i<e[x].size();i++)
    {
        int nxt = e[x][i];
        if (nxt != p)
        {
            dfs(p, x, nxt);
        }
        if (i>0 && arr[nxt] == arr[e[x][i-1]])
        {
            ans[arr[nxt]] = 1;
        }
    }
}
void solve()
{
    cin>>n;
    for(int i=0;i<n;i++)
    {
        cin>>arr[i];
    }
    for(int i=0;i<n-1;i++)
    {
        cin>>u>>v;
        u--,v--;
        e[u].push_back(v);
        e[v].push_back(u);
    }
    dfs(-1, -1, 0);

    for(int i=1;i<=n;i++)
    {
        cout<<ans[i];
    }
    cout<<endl;

    for(int i=0;i<n;i++)
    {
        e[i].clear();
        ans[i+1] = 0;
    }
}
int main()
{
    #ifdef CODEBLOCKS
    freopen("in.txt", "r", stdin);
    #endif // CODEBLOCKS
    int t;
    cin>>t;
    for(int i=0;i<t;i++)
    {
        solve();
    }
    return 0;
}
