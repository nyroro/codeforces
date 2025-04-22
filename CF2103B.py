def solve():
    n = int(input())
    s = input()
    ret = 0

    f01 = 0
    f10 = 0
    if s[0]=='0':
        ret += 1
    else:
        ret += 2
        f01 += 1
    for i in range(1,n):
        if s[i] == s[i-1]:
            ret += 1
        elif s[i] == '0':
            ret += 2
            f10 += 1
        else:
            ret += 2
            f01 +=1
    # print('ret',ret, f01, f10)
    if f01 >= 2 or f10 >= 2:
        ret -= 2
    elif f01 >= 1 and f10 >= 1:
        ret -= 1
    print(ret)

for i in range(int(input())):
    solve()