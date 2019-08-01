#include <iostream>
#include <cstdio>
using namespace std;
 
int main()
{
    #ifdef CODEBLOCKS
    freopen("in.txt", "r", stdin);
    #endif // CODEBLOCKS
    int t;
    cin>>t;
    for(int ti = 0;ti<t;ti++)
    {
 
        int n, x;
        cin>>n>>x;
        cout<<x*2<<endl;
    }
    return 0;
}