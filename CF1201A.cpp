#include <iostream>
#include <cstdio>
using namespace std;
int n,m;
const int N = 1010;
string ans[N];
int point[N];
 
int main()
{
    #ifdef CODEBLOCKS
    freopen("in.txt", "r", stdin);
    #endif // CODEBLOCKS
    while(cin>>n>>m)
    {
        for(int i=0;i<n;i++)
        {
            cin>>ans[i];
        }
        int ret = 0;
        int point;
        for(int i=0;i<m;i++)
        {
            cin>>point;
            int cnt[5];
            for(int j=0;j<5;j++)
            {
                cnt[j] = 0;
            }
 
            for(int j=0;j<n;j++)
            {
                cnt[ans[j][i]-'A'] += 1;
            }
            int num = cnt[0];
            for(int j=0;j<5;j++)
            {
                num = max(num, cnt[j]);
            }
            ret += point * num;
        }
        cout<<ret<<endl;
    }
    return 0;
}