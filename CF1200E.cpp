#include <iostream>
#include <cstdio>
using namespace std;
const int N = 1100010;
char ans[N];
int an;
string str;
int nex[N];

void calNext(string str)
{
    int now = 0;
    int prev = -1;
    int len = str.size();
    nex[0] = -1;
    while(now<len-1)
    {
        if(prev==-1||str[now] == str[prev])
        {
            now++;
            prev++;
            nex[now] = prev;
        }
        else
        {
            prev = nex[prev];
        }
    }
}

int main()
{
    #ifdef CODEBLOCKS
    freopen("in.txt", "r", stdin);
    #endif // CODEBLOCKS
    int n;
    while(cin>>n)
    {
        for(int i=0;i<n;i++)
        {
            cin>>str;
            if(i==0)
            {
                for(int j=0;j<str.size();j++)
                {
                    ans[j] = str[j];
                }
                an = str.size();
            }
            else
            {
                calNext(str);
                int len = str.size();
                int i=max(0, an-len);
                int j=0;
                while(i<an&&j<len)
                {
                    if(j==-1||ans[i]==str[j])
                    {
                        i++;
                        j++;
                    }
                    else
                    {
                        j=nex[j];
                    }
                }
                if(i==an)
                {
                    for(int k=j;k<len;k++)
                    {
                        ans[an++] = str[k];
                    }
                }
            }
        }
        ans[an]='\0';
        cout<<ans<<endl;
    }
    return 0;
}
