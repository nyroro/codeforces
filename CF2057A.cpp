#include <iostream>

using namespace std;
#define max(a,b) ((a)>(b)?(a):(b))
int main()
{
    #ifdef CODEBLOCKS
    freopen("in.txt", "r", stdin);
    #endif // CODEBLOCKS
    int t;
    cin>>t;
    for (int ti=0;ti<t;ti++)
    {
        int n,m;
        cin>>n>>m;
        cout<<max(n,m)+1<<endl;
    }
}
