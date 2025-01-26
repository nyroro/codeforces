#include <iostream>

using namespace std;

int main()
{
    #ifdef CODEBLOCKS
    freopen("in.txt", "r", stdin);
    #endif // CODEBLOCKS
    int t;
    cin>>t;
    for(int ti=0;ti<t;ti++)
    {
        int n,k;
        long long ans=0;
        cin>>n>>k;
        int m = n;
        int p = 1;
        while(m>=k)
        {
            if (m&1)
            {
                ans += 1ll*p*(n+1)/2;
            }
            p<<=1;
            m>>=1;
        }
        cout<<ans<<endl;
    }
    return 0;
}
