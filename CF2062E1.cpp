#include <bits/stdc++.h>
#include <vector>
using namespace std;
#define N 400010
int w[N],ind[N],dfn[N],low[N],s[N];
vector<int> e[N];
int dfs(int p, int x, int num)
{
    dfn[x] = num;
    int m = e[x].size();
    for(int i=0;i<m;i++)
    {
        int nxt = e[x][i];
        if (p != nxt)
        {
            num = dfs(x, nxt, num+1);
        }
    }
    low[x] = num;
    return num;
}
bool cmp(int x, int y)
{
    return w[x]>w[y];
}
int sum(int x)
{
    int ret = 0;
    while(x>0)
    {
        ret += s[x];
        x-=(x&-x);
    }
    return ret;
}
bool gao(int x, int n)
{
    int l = dfn[x];
    int r = low[x];
//    cout<<"gaot"<<x<<' '<<l<<' '<<r<<endl;
//    cout<<"gao"<<x<<' '<<sum(n)<<' '<<sum(r)<<' '<<sum(l-1)<<endl;
    return sum(n)-sum(r)+sum(l-1) > 0;
}
void update(int x, int n)
{
    x = dfn[x];
//    cout<<"update"<<x<<endl;
    while(x<=n)
    {
        s[x]+=1;
        x+=(x&-x);
    }
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
        for(int i=1;i<=n;i++)
        {
            cin>>w[i];
            ind[i] = i;
        }
        for(int i=0;i<n-1;i++)
        {
            cin>>u>>v;
            e[u].push_back(v);
            e[v].push_back(u);
        }
        dfs(0, 1, 1);
        sort(ind+1, ind+n+1, cmp);
        int l = 1, r=1;
        int ans =0;
        while(l<=n)
        {
            while (r<=n &&w[ind[r]]==w[ind[l]])r++;
//            cout<<l<<' '<<r<<endl;
            for (int i = l;i<r;i++)
            {
                if (gao(ind[i], n))
                {
                    ans = ind[i];
                    break;
                }
            }
            if (ans > 0)break;
            for(int i=l;i<r;i++)
            {
                update(ind[i], n);
            }
            l = r;
        }
        cout<<ans<<endl;

        for(int i=1;i<=n;i++)
        {
            s[i] = 0;
            e[i].clear();
        }
    }
}
