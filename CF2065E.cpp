#include <bits/stdc++.h>

using namespace std;
#define N 400010
int arr[N];
void solve()
{
    int n,m,k;
    cin>>n>>m>>k;
    int a = max(n,m);
    int b = min(n,m);
    if(a-b>k||a<k)
    {
        cout<<-1<<endl;
    }
    else
    {
        for(int i=0;i<k;i++)
        {
            arr[i]=0;
        }
        a-=k;
        int x = k;
        while(a>0 &&b>0)
        {
            arr[x] = 1;
            arr[x+1]=0;
            x+=2;
            a--;
            b--;
        }
        while(b>0)
        {
            arr[x]=1;
            b--;
            x++;
        }
        while(a>0)
        {
            a--;
            arr[x]=0;
            x++;
        }
        for(int i=0;i<n+m;i++)
        {
            cout<<(n>m?arr[i]:1-arr[i]);
        }
        cout<<endl;
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
