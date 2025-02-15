t = int(input())
def solve(a,b,c,d,e):
    ret = 0
    if a+b==c:
        ret += 1
    if b+c == d:
        ret+=1
    if c+d==e:
        ret+=1
    return ret
for _ in range(t):
    a,b,c,d = map(int, input().split())
    ans1 =solve(a,b,a+b,c,d)
    ans2 = solve(a,b,c-b,c,d)
    ans3 = solve(a,b,d-c,c,d)
    print(max(ans1,ans2,ans3))

    