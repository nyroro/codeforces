#include <iostream>
#include <set>
#include <vector>
#include <map>
#include <queue>
#include <bits/stdc++.h>
using namespace std;
#define N 1001
int n,s1,s2;
int m1,m2;
vector<int> g1[N], g2[N];
set<int> es;
map<int,int> d;
pair<int,int> fromid(int x)
{
    int a = x/N;
    int b = x%N;
    return make_pair(a,b);
}
int toid(int x,int y)
{
    return x*N+y;
}
int spfa()
{
    priority_queue<pair<int,int>> q;
    int x = toid(s1, s2);
    d[x] = 0;
    q.push(make_pair(0, x));

    while (!q.empty())
    {
        pair<int, int> p = q.top();
        q.pop();
        int v = -p.first;
        int id = p.second;
        if (d[id]<v)
        {
            continue;
        }
        pair<int,int> pid = fromid(id);
        int x = pid.first;
        int y = pid.second;
        for (int i=0;i<g1[x].size();i++)
        {
            for(int j=0;j<g2[y].size();j++)
            {
                int tx = g1[x][i];
                int ty = g2[y][j];
                if (x == y &&tx == ty)
                {
                    return v;
                }
                int tv = v + abs(tx - ty);
                int tid = toid(tx,ty);
                if (d.find(tid) ==d.end() || d[tid]>tv)
                {
                    d[tid] = tv;
                    q.push(make_pair(-tv, tid));
                }
            }
        }
    }

    return -1;
}
void solve()
{
    cin>>n>>s1>>s2;
    cin>>m1;
    int u,v;
    for(int i=0;i<m1;i++)
    {
        cin>>u>>v;
        g1[u].push_back(v);
        g1[v].push_back(u);
        if (u>v)
        {
            int tmp = u;
            u = v;
            v = tmp;
        }
        es.insert(u*N+v);
    }
    bool flag = false;
    cin>>m2;
    for(int i=0;i<m2;i++)
    {
        cin>>u>>v;
        g2[u].push_back(v);
        g2[v].push_back(u);
        if (u>v)
        {
            int tmp = u;
            u = v;
            v = tmp;
        }
        if (!flag && es.find(u*N+v)!=es.end())
        {
            flag = true;
        }
    }
    if (!flag)
    {
        cout<<-1<<endl;
    }
    else
    {
        cout<<spfa()<<endl;
    }
    for(int i=1;i<=n;i++)
    {
        g1[i].clear();
        g2[i].clear();
    }
    d.clear();
    es.clear();
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
        solve();
    }
    return 0;
}
