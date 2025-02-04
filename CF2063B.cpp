#include <iostream>
#include <bits/stdc++.h>
#include <queue>
using namespace std;
#define N 100001
priority_queue<int> q1,q2;
int main()
{
    #ifdef CODEBLOCKS
    freopen("in.txt", "r", stdin);
    #endif // CODEBLOCKS
    int t;
    cin>>t;
    for(int ti = 0; ti<t;ti++)
    {
        int n,l,r,a;
        cin>>n>>l>>r;
        for(int i=0;i<n;i++)
        {
            cin>>a;
            if (i<=r-1)
            {
                q1.push(a);
                if (q1.size() > r-l+1)
                {
                    q1.pop();
                }
            }
            if (i>=l-1)
            {
                q2.push(a);
                if (q2.size() > r-l+1)
                {
                    q2.pop();
                }
            }
        }
        long long ans1 = 0, ans2 = 0;
        while(q1.size()>0)
        {
            ans1+=q1.top();
            q1.pop();
        }
        while(q2.size()>0)
        {
            ans2+=q2.top();
            q2.pop();
        }
        cout<<min(ans1,ans2)<<endl;
    }
    return 0;
}
