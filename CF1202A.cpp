#include <iostream>
#include <cstdio>
using namespace std;
string a,b;
int main()
{
    #ifdef CODEBLOCKS
    freopen("in.txt","r",stdin);
    #endif // CODEBLOCKS
    int t;
    cin>>t;
    for(int ti=0;ti<t;ti++)
    {
        cin>>a>>b;
        int tb;
        int lb = b.size();
        for(int i=0;i<lb;i++)
        {
            if(b[lb-i-1]=='1')
            {
                tb = i;
                break;
            }
        }
        int ta=0;
        int la = a.size();
        if(tb>=la)
        {
            ta = 0;
        }
        else
        {
            for(int i=0;i<la;i++)
            {
                int index = la-i-1-tb;
                if(index<0)break;
                if(a[index] == '1')
                {
                    ta = i;
                    break;
                }
            }
        }
        cout<<ta<<endl;
    }
    return 0;
}