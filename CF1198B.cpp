#include <iostream>
#include <cstdio>
using namespace std;
int n;
const int N = 2*100001;
int arr[N];
int q;
struct seg
{
    int l,r;
    int val;
    seg(){}
    seg(int l, int r):l(l),r(r){}

}segs[N*4];
seg build_tree(int root, int l, int r)
{
    segs[root] = seg(l, r);
    if(l==r)
    {
        segs[root].val = arr[l];
    }
    else
    {
        int mid = (l+r)/2;
        build_tree(2*root, l, mid);
        build_tree(2*root+1, mid+1, r);
        segs[root].val = min(segs[2*root].val, segs[2*root+1].val);
    }
}
void apply(int root, int index, int val)
{
//    cout<<"apply"<<segs[root].l <<' '<< segs[root].r<<' '<<index<<' '<<val<<endl;
    if(segs[root].l == segs[root].r)
    {
        if(segs[root].l == index)
        {
            arr[index] = val;
            segs[root].val = val;
        }
        else
        {
            if(segs[root].val > arr[segs[root].l])
            {
                arr[segs[root].l] = segs[root].val;
            }
        }
        return;
    }
    if(segs[root].l<=index && index<=segs[root].r)
    {
        seg left = segs[2*root];
        seg right = segs[2*root + 1];
        if(left.val < segs[root].val)
        {
            segs[2*root].val = segs[root].val;
        }
        if(right.val < segs[root].val)
        {
            segs[2*root+1].val = segs[root].val;
        }
        if(left.l<=index && index<=left.r)
        {
            apply(2*root, index, val);
        }
        else
        {
            apply(2*root, index, segs[root].val);
        }
        if(right.l<=index &&index<=right.r)
        {
            apply(2*root+1, index, val);
        }
        else
        {
            apply(2*root+1, index, segs[root].val);
        }
        segs[root].val = min(segs[2*root].val, segs[2*root+1].val);
    }
    else
    {
        if(val>segs[root].val)
        {
            segs[root].val = val;
        }
    }
}
void applyFinal(int root, int val)
{
//    cout<<"apply final"<<segs[root].l <<' '<< segs[root].r<<' '<<segs[root].val<<endl;
    if(segs[root].l == segs[root].r)
    {
        arr[segs[root].l] = max(segs[root].val, val);
        return;
    }
    applyFinal(2*root, max(val, segs[root].val));
    applyFinal(2*root+1, max(val, segs[root].val));
}
int main()
{
    #ifdef CODEBLOCKS
    freopen("in.txt","r", stdin);
    #endif // CODEBLOCKS
    while(cin>>n)
    {
        for(int i=0;i<n;i++)
        {
            cin>>arr[i];
        }
        build_tree(1, 0, n-1);
//        cout<<"build end"<<endl;
        cin>>q;
        for(int i=0;i<q;i++)
        {
            int t,p,x;
            cin>>t;
            if(t==1)
            {
                cin>>p>>x;
                apply(1, p-1, x);
//                for(int i=0;i<n;i++)
//                {
//                    cout<<arr[i]<<' ';
//                }
//                cout<<endl;
            }
            else
            {
                cin>>x;
                if(x > segs[1].val)
                {
                    segs[1].val = x;
                }
            }
        }
        applyFinal(1, segs[1].val);
        for(int i=0;i<n;i++)
        {
            if(i)cout<<' ';
            cout<<arr[i];
        }
        cout<<endl;
    }
    return 0;
}
