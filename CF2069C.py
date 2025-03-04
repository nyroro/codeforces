mod = 998244353
def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    one = [0]*n
    one[0] = 1 if arr[0] == 1 else 0
    two = [0]*n
    ans = 0
    for i in range(1, n):
        one[i] = one[i-1]
        if arr[i] == 1:
            one[i]+=1
        if arr[i] == 2:
            two[i]+=one[i-1]
            two[i]+=two[i-1]
            two[i]%=mod
        two[i]+=two[i-1]
        two[i]%=mod
        if arr[i]==3:
            ans += two[i-1]
            ans %= mod
    print(ans)
    
for i in range(int(input())):
    solve()