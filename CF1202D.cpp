#include <iostream>
 
using namespace std;
const int N = 400;
const int X = (400*399)/2;
int main()
{
    int t;
    cin>>t;
    for(int ti=0;ti<t;ti++)
    {
        int n;
        cin>>n;
        if(n<X)
        {
            cout<<133;
            for(int i=0;i<n;i++)
            {
                cout<<7;
            }
            cout<<endl;
        }
        else
        {
            int n1 = n/X;
            int n2 = n%X;
            cout<<133;
            for(int i=0;i<n2;i++)
            {
                cout<<7;
            }
            for(int i=0;i<N-2;i++)
            {
                cout<<3;
            }
            for(int i=0;i<n1;i++)
            {
                cout<<7;
            }
            cout<<endl;
        }
    }
    return 0;
}