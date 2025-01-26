#include <iostream>
#include<bits/stdc++.h>
using namespace std;
#define N 800001
int ans[N],t0[N],t1[N],t2[N],t3[N];
void update(int u, int l, int r, int x, int v)
{
    if (l==r)
    {
        ans[u] = 0;
        t0[u]=v+l;
        t1[u] = -v+l;
        t2[u] = v-l;
        t3[u] = -v-l;
        return;
    }
    int m = (l+r)/2;
    if (x<=m)
    {
        update(u*2, l,m,x,v);
    }
    else
    {
        update(u*2+1, m+1, r, x,v);
    }
    ans[u]=max({ans[u*2],ans[u*2+1],t0[u*2]+t3[u*2+1],t1[u*2]+t2[u*2+1]});
	t0[u]=max(t0[u*2],t0[u*2+1]);
	t1[u]=max(t1[u*2],t1[u*2+1]);
	t2[u]=max(t2[u*2],t2[u*2+1]);
	t3[u]=max(t3[u*2],t3[u*2+1]);
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
        int n,q,u,v;
        cin>>n>>q;
        for(int i=1;i<=n;i++)
        {
            cin>>v;
            update(1,1,n,i,v);
        }
        cout<<ans[1]<<endl;
        for(int i=0;i<q;i++)
        {
            cin>>u>>v;
            update(1,1,n,u,v);
            cout<<ans[1]<<endl;
        }

    }
}
