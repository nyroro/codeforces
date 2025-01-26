#include <iostream>

using namespace std;
#define N 400010
int l[N],r[N],cnt[N],pre[N];
int main()
{
    #ifdef CODEBLOCKS
    freopen("in.txt", "r", stdin);
    #endif // CODEBLOCKS
    int t;
    cin>>t;
    for(int ti=0;ti<t;ti++)
    {
        int n;
        cin>>n;
        for(int i=0;i<=2*n;i++)
        {
            cnt[i] = 0;
            pre[i] = 0;
        }
        for(int i=0;i<n;i++)
        {
            cin>>l[i]>>r[i];
            cnt[l[i]] += (int)(l[i]==r[i]);
        }
        for(int i=0;i<=2*n;i++)
        {
            pre[i] = cnt[i]>0?1:0;
            if (i>0)
            {
                pre[i]+=pre[i-1];
            }
        }
        for(int i=0;i<n;i++)
        {
            if (l[i]==r[i])
            {
                cout<<(cnt[l[i]]==1?1:0);
            }
            else
            {
                if (pre[r[i]]-pre[l[i]-1] == r[i]-l[i]+1)
                {
                    cout<<0;
                }
                else
                {
                    cout<<1;
                }
            }
        }
        cout<<endl;
    }
    return 0;
}
