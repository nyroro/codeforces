t = int(input())
for _ in range(t):
    n = int(input())
    a = n//15
    b = n%15
    print(a*3 + min(b, 2)+1)