#include <iostream>
#include <cstdio>
using namespace std;
long long n,m;
int q;
long long gcd(long long a, long long b)
{
    if(a<b)
    {
        swap(a,b);
    }
    while(b!=0)
    {
        long long t = a%b;
        a = b;
        b = t;
    }
    return a;
}
int main()
{
    #ifdef CODEBLOCKS
    freopen("in.txt", "r", stdin);
    #endif // CODEBLOCKS
    cin>>n>>m>>q;
    long long g = gcd(n,m);
    long long t1 = n/g;
    long long t2 = m/g;
    for(int i=0;i<q;i++)
    {
        long long x1,y1,x2,y2;
        cin>>x1>>y1>>x2>>y2;
        y1--;
        y2--;
        long long r1,r2;
        if(x1 == 1)r1 = y1/t1;
        else r1 = y1/t2;
    
        if(x2 == 1)r2 = y2/t1;
        else r2 = y2/t2;
//        cout<<r1<<' '<<r2<<endl;
        cout<<(r1==r2?"YES":"NO")<<endl;
    }
    return 0;
}