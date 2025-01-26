#include <iostream>
#include <bits/stdc++.h>
using namespace std;
#define MAXN 200010
vector<int> g[MAXN];
int d[MAXN];
long long solve(int n)
{
    long long ans=0;
    int cnt = 0, cnt2=0;
    for(int i=0;i<n;i++)
    {
        if (g[i].size()==1)
        {
            cnt+=1;
        }
        else
        {

            for(int v:g[i])
            {
                d[i] += (g[v].size() > 1);
            }
            cnt2+=(d[i] == g[i].size());
        }
    }
    ans += 1ll*cnt*(n-cnt);
    for (int i=0;i<n;i++)
    {
        int gn = g[i].size();
        if (gn>1 &&d[i]!=gn)
        {
            ans += 1ll*cnt2*(d[i]-1);
        }
    }
    return ans;
}
int main()
{
    #ifdef CODEBLOCKS
    freopen("in.txt", "r", stdin);
    #endif // CODEBLOCKS
    int t;
    cin>>t;
    for(int ti=0;ti<t;ti++)
    {
        int n,u,v;
        cin>>n;
        for(int i=0;i<n-1;i++)
        {
            cin>>u>>v;
            g[u-1].push_back(v-1);
            g[v-1].push_back(u-1);
        }
        cout<<solve(n)<<endl;
        for(int i=0;i<n;i++)
        {
            g[i].clear();
            d[i] = 0;
        }
    }
    return 0;
}
