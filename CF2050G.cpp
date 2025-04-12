#include <iostream>
#include <vector>
using namespace std;
#define N 200010
vector<int> graph[N];
int dp[N];
int ret[N];

void dfs(int x, int pre)
{
    int child = graph[x].size()-1;
    if (pre < 0)
    {
        child+=1;
    }
    dp[x] = child;
    ret[x] = graph[x].size();
    int m1 = 0;
    int m2 = 0;
    for(int i=0;i<graph[x].size();i++)
    {
        int nxt = graph[x][i];
        if (nxt != pre)
        {
            dfs(nxt, x);
            dp[x] = max(dp[x], child - 1 + dp[nxt]);
            if (dp[nxt] > m1)
            {
                m2 = m1;
                m1 = dp[nxt];
            }
            else if (dp[nxt]>m2)
            {
                m2 = dp[nxt];
            }
            int val = dp[x]+1;
            if (pre < 0)
            {
                val -= 1;
            }
            ret[x] = max(ret[x], val);
            val = m1+m2+child-1;
            if (pre < 0)
            {
                val -= 1;
            }
            ret[x] = max(ret[x], val);
        }
    }
}
void solve()
{
    int n,u,v;
    cin>>n;
    for(int i=0;i<n-1;i++)
    {
        cin>>u>>v;
        graph[u-1].push_back(v-1);
        graph[v-1].push_back(u-1);
    }
    for(int i=0;i<n;i++)
    {
        dp[i]=ret[i]=0;
    }
    dfs(0, -1);
    int ans = 0;
    for(int i=0;i<n;i++)
    {
        ans=max(ans,ret[i]);
    }

    cout<<ans<<endl;
    for(int i=0;i<n;i++)
    {
        graph[i].clear();
    }
}
int main()
{
    #ifdef CODEBLOCKS
    freopen("in.txt","r",stdin);
    #endif // CODEBLOCKS
    int t;
    cin>>t;
    for(int i=0;i<t;i++)
    {
        solve();
    }
    return 0;
}
