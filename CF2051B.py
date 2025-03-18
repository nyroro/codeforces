def solve():
    n,a,b,c = map(int, input().split())
    x = n//(a+b+c)*3
    y = n%(a+b+c)
    if 0<y<=a:
        x+=1
    elif a<y<=a+b:
        x+=2
    elif a+b<y<a+b+c:
        x+=3
    print(x)
for i in range(int(input())):
    solve()