#include <iostream>
#include <cstdio>
using namespace std;
int n,m,k;
int h[110];
int main()
{
    #ifdef CODEBLOCKS
    freopen("in.txt","r",stdin);
    #endif // CODEBLOCKS
    int t;
    cin>>t;
    for(int ti=0;ti<t;ti++)
    {
        cin>>n>>m>>k;
        for(int i=0;i<n;i++)
        {
            cin>>h[i];
        }
        bool flag = true;
        for(int i=0;i<n-1;i++)
        {
            int to_next = max(0, h[i+1]-k);
            if(h[i]>to_next)
            {
                m+=h[i]-to_next;
            }
            else
            {
                m-=to_next - h[i];
            }
            if(m<0)
            {
                flag = false;
                break;
            }
        }
        if(flag)
        {
            cout<<"YES"<<endl;
        }
        else
        {
            cout<<"NO"<<endl;
        }
    }
    return 0;
}