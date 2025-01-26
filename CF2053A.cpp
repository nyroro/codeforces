#include <iostream>

using namespace std;

int arr[300];
int main()
{

    #ifdef CODEBLOCKS
    freopen("in.txt", "r", stdin);
    #endif // CODEBLOCKS
    int t;
    cin>>t;
    for(int ti=0;ti<t;ti++)
    {
        int n;
        cin>>n;
        bool flag = false;
        for(int i=0;i<n;i++)
        {
            cin>>arr[i];
            if (i>0 && min(arr[i],arr[i-1]) * 2 >max(arr[i],arr[i-1]))
            {
                flag = true;
            }
        }
        if (flag)
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
