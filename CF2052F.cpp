#include <iostream>

using namespace std;
string a,b;
int dp[4],ndp[4];
int main()
{
    #ifdef CODEBLOCKS
    freopen("in.txt", "r", stdin);
    #endif // CODEBLOCKS
    int t=0;
    cin>>t;
    for(int ti=0;ti<t;ti++)
    {
        int n;
        cin>>n;
        cin>>a>>b;
        dp[3] = 1;
        dp[1]=dp[2]=dp[0]=0;
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<4;j++)
            {
                ndp[j] = 0;
            }
            if (a[i]=='.' && b[i] == '.')
            {
                ndp[3]+=dp[0]+dp[3];
                ndp[0]+=dp[3];
                ndp[1]+=dp[2];
                ndp[2]+=dp[1];
            }
            else if (a[i]=='#'&&b[i]=='#')
            {
                ndp[3]+=dp[3];
            }
            else if(a[i]=='#')
            {
                ndp[3]+=dp[1];
                ndp[1]+=dp[3];
            }
            else if(b[i]=='#')
            {
                ndp[3]+=dp[2];
                ndp[2]+=dp[3];
            }
            for(int i=0;i<4;i++)
            {
                dp[i] = min(ndp[i], 2);
            }
        }
        if (dp[3]==0)
        {
            cout<<"None"<<endl;
        }
        else if(dp[3]==1)
        {
            cout<<"Unique"<<endl;
        }
        else
        {
            cout<<"Multiple"<<endl;
        }
    }

    return 0;
}
