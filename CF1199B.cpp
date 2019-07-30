#include <iostream>
#include <cstdio>
using namespace std;
int h,l;
int main()
{
    #ifdef CODEBLOCKS
    freopen("in.txt", "r", stdin);
    #endif // CODEBLOCKS
    while(cin>>h>>l)
    {
        printf("%.7f\n",(1.0*l/2/h*l - 1.0*h/2));
    }
    return 0;
}
