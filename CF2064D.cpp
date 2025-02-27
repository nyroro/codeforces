#include <bits/stdc++.h>

using namespace std;
#define N 200010
#define M 30
int w[N];
int xorarr[N];
int last[N][M];
void solve()
{
    int n,q;
    cin>>n>>q;
    for(int i=0;i<n;i++)
    {
        cin>>w[i];
    }
    int now = 0;
    for(int i=n-1;i>=0;i--)
    {
        now ^= w[i];
        xorarr[i] = now;
    }
    xorarr[n] = 0;
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<M;j++)
        {
            last[i][j] = i>0?last[i-1][j]:0;
        }
        int lg = __lg(w[i]);
        last[i][lg] = i;
        for (int j=M-2;j>=0;j--)
        {
            last[i][j] = max(last[i][j],last[i][j+1]);
        }
    }
    bool flag = false;
    while(q--)
    {
        int x;
        cin>>x;
        int idx = n-1;
        while (idx>=0&&x>0)
        {
            int val = x^xorarr[idx+1];
            if (val <= 0)
            {
                break;
            }
            int lg = __lg(val);
            int nxt = last[idx][lg];
            val = x ^ xorarr[nxt+1];
            idx = nxt;
            if (w[nxt]>val)break;
            idx--;
        }
        if (flag)
        {
            cout<<' ';
        }
        else
        {
            flag = true;
        }

        cout<<n-idx-1;
    }
    cout<<endl;
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
