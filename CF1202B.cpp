#include <iostream>
#include <cstdio>
using namespace std;
int ret[10][10];
int dp[10][10];
bool vis[10];
 
string str;
void calDP(int x, int y)
{
    for(int i=0;i<10;i++)
    {
        for(int j=0;j<10;j++)
        {
            dp[i][j] = -1;
            vis[j] = false;
        }
        vis[(i+x)%10] = true;
        dp[i][(i+x)%10]=0;
        vis[(i+y)%10] = true;
        dp[i][(i+y)%10]=0;
        int que[11];
        int qn,qi;
        qn = qi = 0;
        que[qn++] = (i+x)%10;
        que[qn++] = (i+y)%10;
//        if(x==1&&y==1)
//        {
//
//            cout<<"start"<<i<<endl;
//        }
        while(qi<qn)
        {
            int now = que[qi++];
            int nex1 = (now+x)%10;
            int nex2 = (now+y)%10;
//            if(x==1&&y==1)
//            {
//                cout<<i<<' '<<now<<' '<<nex1<<' '<<nex2<<endl;
//
//            }
            if(!vis[nex1])
            {
                dp[i][nex1] = dp[i][now]+1;
                vis[nex1] = true;
                que[qn++] = nex1;
            }
            if(!vis[nex2])
            {
                dp[i][nex2] = dp[i][now]+1;
                vis[nex2] = true;
                que[qn++] = nex2;
            }
        }
    }
//    if(x==1&&y==1)
//    {
//        for(int i=0;i<10;i++)
//        {
//            for(int j=0;j<10;j++)
//            {
//                cout<<dp[i][j]<<' ';
//            }
//            cout<<endl;
//        }
//    }
 
}
int main()
{
    #ifdef CODEBLOCKS
    freopen("in.txt", "r", stdin);
    #endif // CODEBLOCKS
    cin>>str;
    //Count zero
    bool allZero = true;
    int n = str.size();
 
    for(int i=0;i<10;i++)
    {
        for(int j=0;j<10;j++)
        {
            calDP(i, j);
            int res = 0;
            for(int k=1;k<n;k++)
            {
                int l = str[k-1]-'0';
                int r = str[k]-'0';
                if(dp[l][r]>=0)
                {
                    res+=dp[l][r];
                }
                else
                {
                    res=-1;
                    break;
                }
            }
            if(j)cout<<' ';
            cout<<res;
        }
        cout<<endl;
    }
    return 0;
}