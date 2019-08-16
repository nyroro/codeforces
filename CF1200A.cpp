#include <iostream>
#include <cstdio>
using namespace std;
int main()
{
    #ifdef CODEBLOCKS
    freopen("in.txt","r",stdin);
    #endif // CODEBLOCKS
    int n;
    while(cin>>n)
    {
        string str;
        bool room[10];
        for(int i=0;i<10;i++)room[i] = false;
        cin>>str;
        int m = str.size();
        for(int i=0;i<m;i++)
        {
            if(str[i]=='L')
            {
                for(int j=0;j<10;j++)
                {
                    if(!room[j])
                    {
                        room[j]=true;
                        break;
                    }
                }
            }
            else if(str[i]=='R')
            {
                for(int j=9;j>=0;j--)
                {
                    if(!room[j])
                    {
                        room[j]=true;
                        break;
                    }
                }
            }
            else
            {
                room[str[i]-'0'] = false;
            }
        }
    
        for(int i=0;i<10;i++)
        {
            cout<<room[i]?1:0;
        }
        cout<<endl;
    }
    return 0;
}