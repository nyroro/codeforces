mod = int(1e9)+7
def solve():
    n = int(input())
    s = input()
    ret = n-1
    for i in range(1,n):
        if s[i] == '1':
            ret += pow(2, i*(mod-2), mod)
            ret %= mod
    print(ret)
for i in range(int(input())):
    solve()