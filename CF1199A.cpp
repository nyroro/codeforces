#include <iostream>
#include <cstdio>
#include <queue>
using namespace std;
int n, x, y;
const int N = 100002;
int arr[N];
bool valid[N];

int main()
{
    #ifdef CODEBLOCKS
    freopen("in.txt", "r", stdin);
    #endif // CODEBLOCKS

    while(cin>>n>>x>>y)
    {
        for(int i=0;i<n;i++)
        {
            cin>>arr[i];
            valid[i] = false;
        }
        for(int i=0;i<n;i++)
        {
            bool flag = true;
            for(int j=0;j<x&&i-j-1>=0;j++)
            {
                if(arr[i]>=arr[i-j-1])
                {
                    flag = false;
                    break;
                }
            }
            valid[i] = flag;
        }
//        for(int i=0;i<n;i++)
//        {
//            cout<<valid[i]<<' ';
//        }
//        cout<<endl;

        for(int i=0;i<n;i++)
        {
            bool flag = true;
            for(int j=0;j<y&&i+j+1<n;j++)
            {
                if(arr[i]>=arr[i+j+1])
                {

                    flag = false;
                    break;
                }
            }
            if(valid[i] && flag)
            {
                cout<<i+1<<endl;
                break;
            }
        }
    }
    return 0;
}
