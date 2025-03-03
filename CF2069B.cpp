#include <bits/stdc++.h>

using namespace std;

#define N 705
int arr[N][N];
set<int> s1;
set<int> s2;
void solve()
{
    s1.clear();
    s2.clear();
    int n,m;
    cin>>n>>m;
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<m;j++)
        {
            cin>>arr[i][j];
        }
    }
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<m;j++)
        {
            int v = arr[i][j];
            if(s1.find(v)==s1.end())
            {
                s1.insert(v);
            }
            if(s2.find(v)==s2.end())
            {
                if(i+1<n&&arr[i+1][j]==v)
                {
                    s2.insert(v);
                }
                else if(j+1<m&&arr[i][j+1]==v)
                {
                    s2.insert(v);
                }
            }
        }
    }
    int ret = s1.size()-1;
    if (s2.size()>0)
    {
        ret += s2.size()-1;
    }
    cout<<ret<<endl;
}
int main()
{
    cin.tie(0);
    cout.tie(0);
    ios_base::sync_with_stdio(0);
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
