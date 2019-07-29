#include <iostream>
#include <cstdio>
#include <algorithm>
#include <map>
using namespace std;
int n;
const int N = 2*1e5+10;
pair<int, int> p[N];
pair<int, long long> dp[N];
const int mod = 1e9+7;
int main()
{
#ifdef CODEBLOCKS
    freopen("in.txt", "r", stdin);
#endif // CODEBLOCKS
    while(cin>>n)
    {
        int min_out = 0x7fffffff;
        for(int i=0;i<n;i++)
        {
            int a,b;
            cin>>a>>b;
            p[i] = make_pair(b,a);
        }
        sort(p, p+n);
        for(int i=n-1;i>=0;i--)
        {
            int in = p[i].first;
            int out = p[i].second;
            auto iter = lower_bound(p, p+n, make_pair(out,0));
            int space, cnt;
            if((iter-p) == n)
            {
                space = in;
                cnt = 1;
            }
            else
            {
                space = dp[iter - p].first - out + in;
                cnt = dp[iter-p].second;
            }
 
            if(i<n-1)
            {
                if(space > dp[i+1].first)
                {
                    space = dp[i+1].first;
                    cnt = dp[i+1].second;
                }
                else if(space == dp[i+1].first)
                {
                    cnt = (cnt + dp[i+1].second)%mod;
                }
            }
            dp[i] = make_pair(space, cnt);
        }
        cout<<dp[0].second<<endl;
    }
    return 0;
}