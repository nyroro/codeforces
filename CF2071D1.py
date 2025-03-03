def cal(x, n, ans):
    if x <= 2*n:
        return ans[x//2]
    k = x//2
    if (k&1)>0:
        return ans[n]
    return ans[n]^cal(k, n,  ans)
def solve():
    n,l,r = map(int, input().split())
    arr = list(map(int, input().split()))
    ans = [0]
    
    if l <= n:
        print(arr[l-1])
        return
    
    for t in arr:
        ans.append(ans[-1]^t)
    if (n&1) == 0:
        ans.append(ans[n//2]^ans[-1])
        n+=1
    print(cal(l,n,ans))
    
for _ in range(int(input())):
    solve()