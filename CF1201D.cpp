#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;
int n,m,k,q;
const int N = 2*100010;
pair<int, int> treasure[N];
int b[N];
#define min(a,b) ((a)<(b)?(a):(b))
int path(int u, int v)
{
    if(u>v)
    {
        swap(u,v);
    }
    int *pu = lower_bound(b,b+q,u);
    int *pv = lower_bound(b,b+q,v);
    if(*pu<=v&&*pu>=u)
        return v-u;
    int ret = 0x7fffffff;
    if(pv-b<q)
    {
        ret = min(ret, (*pv)-v+(*pv)-u);
    }
    if(pu-b>0)
    {
        int left = *(pu-1);
        ret = min(ret, v-left+u-left);
    }
    return ret;
 
}
int main()
{
#ifdef CODEBLOCKS
    freopen("in.txt", "r", stdin);
#endif // CODEBLOCKS
    while(cin>>n>>m>>k>>q)
    {
        for(int i=0; i<k; i++)
        {
            int a,b;
            cin>>a>>b;
            treasure[i] = make_pair(a,b);
        }
        sort(treasure, treasure+k);
        for(int i=0; i<q; i++)
        {
            cin>>b[i];
        }
        sort(b,b+q);
        int preLeft = 1;
        int preRight = 1;
        int preRow = 1;
        // HANDLE FIRST LINE
        int i=0;
        int nowRow = treasure[0].first;
        int minY = treasure[0].second;
        int maxY = treasure[0].second;
        for(; i<k; i++)
        {
            int x = treasure[i].first;
            int y = treasure[i].second;
            if(x==nowRow)
            {
                minY = min(minY, y);
                maxY = max(maxY, y);
            }
            else
            {
                break;
            }
        }
        long long dp[2];
        if(nowRow == preRow)
        {
            dp[1] = maxY-preLeft;
            dp[0] = maxY-preLeft+maxY-minY;
        }
        else
        {
            dp[1] = path(preLeft, minY)+(maxY - minY) + nowRow - preRow;
            dp[0] = path(preLeft, maxY)+(maxY - minY) + nowRow - preRow;
        }
        if(i==k)
        {
            cout<<min(dp[0], dp[1])<<endl;
            continue;
        }
//        cout<<dp[0]<<' '<<dp[1]<<endl;
        preLeft = minY;
        preRight = maxY;
        preRow = nowRow;
 
        int x = treasure[i].first;
        int y = treasure[i].second;
 
        nowRow = x;
        minY = maxY = y;
        for(; i<k; i++)
        {
            int x = treasure[i].first;
            int y = treasure[i].second;
            if(x == nowRow)
            {
                minY = min(minY, y);
                maxY = max(maxY, y);
            }
            else
            {
                long long toLeft = dp[0]+path(preLeft, maxY) + (maxY-minY);
                toLeft = min(toLeft, dp[1]+path(preRight, maxY)+maxY-minY);
                long long toRight = dp[0]+path(preLeft, minY)+(maxY-minY);
                toRight = min(toRight, dp[1]+path(preRight, minY)+maxY-minY);
                dp[0] = toLeft + nowRow - preRow;
                dp[1] = toRight + nowRow - preRow;
//                cout<<dp[0]<<' '<<dp[1]<<endl;
                preLeft = minY;
                preRight = maxY;
                preRow = nowRow;
 
                nowRow = x;
                minY = y;
                maxY = y;
 
            }
        }
 
        long long toLeft = dp[0]+path(preLeft, maxY) + (maxY-minY);
        toLeft = min(toLeft, dp[1]+path(preRight, maxY)+maxY-minY);
        long long toRight = dp[0]+path(preLeft, minY)+(maxY-minY);
        toRight = min(toRight, dp[1]+path(preRight, minY)+maxY-minY);
        dp[0] = toLeft + nowRow - preRow;
        dp[1] = toRight + nowRow - preRow;
//        cout<<dp[0]<<' '<<dp[1]<<endl;
 
        cout<<min(dp[0], dp[1])<<endl;
 
 
    }
    return 0;
}