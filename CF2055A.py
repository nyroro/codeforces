t = int(input())
for _ in range(t):
    n,a,b = map(int, input().split())
    if abs(b-a) & 1 == 0:
        print("YES")
    else:
        print("NO") 