#include <iostream>

using namespace std;

int main()
{
    #ifdef CODEBLOCKS
    freopen("in.txt", "r", stdin);
    #endif // CODEBLOCKS
    int t;
    cin >> t;
    for(int ti=0;ti<t;ti++)
    {
        int l,r;
        cin>>l>>r;
        int k = l^r;
        int a = 0;
        int b = 0;
        for(int i=30;i>=0;i--)
        {
            if ((k & (1<<i)) != 0)
            {
                a |= (1<<i);
                b |= (1<<i)-1;
                break;
            }
            else
            {
                a|= l&(1<<i);
                b|= l&(1<<i);
            }
        }
        int c = l;
        while (c == a||c==b)
        {
            c++;
        }

        cout<<a<<' '<<b<<' '<<c<<endl;
    }
    return 0;
}
