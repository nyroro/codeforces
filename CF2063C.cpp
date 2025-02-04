    #include <iostream>
    #include <vector>
    #include <algorithm>
    using namespace std;
    #define N 200010
    vector<int> edg[N];
    int deg[N];
    int sdeg[N];
    bool cmp(int a, int b)
    {
        return deg[a]>deg[b];
    }
    int main()
    {
        #ifdef CODEBLOCKS
        freopen("in.txt", "r", stdin);
        #endif // CODEBLOCKS
        int t;
        cin>>t;
        for(int ti=0;ti<t;ti++)
        {
            int n,a,b;
            cin>>n;
            int ans = 1;
            for(int i=0;i<n-1;i++)
            {
                cin>>a>>b;
                a--;
                b--;
                edg[a].push_back(b);
                edg[b].push_back(a);
            }
            for(int i=0;i<n;i++)
            {
                deg[i] = sdeg[i] = edg[i].size();
            }
            if (n==2)
            {
                ans = 0;
            }
            else
            {
                sort(sdeg,sdeg+n);
                for(int i=0;i<n;i++)
                {
                    int tans = deg[i]-1;
                    sort(edg[i].begin(), edg[i].end(), cmp);
                    if (deg[i]<deg[edg[i][0]])
                    {
                        continue;
                    }
                    int point = n-1;
                    if (deg[i] == sdeg[point])
                    {
                        point-=1;
                    }
                    for(int j =0;j<edg[i].size();j++)
                    {
                        int to = edg[i][j];
                        int tdeg = deg[to];
                        ans = max(ans, tans+tdeg -1);
                        if (sdeg[point] == tdeg)
                        {
                            point-=1;
                        }
                        else
                        {
                            ans = max(ans, tans+sdeg[point]);
                            break;
                        }
                    }
                }

            }


            cout<<ans<<endl;

            for(int i=0;i<n;i++)
            {
                edg[i].clear();
            }
        }
        return 0;
    }
