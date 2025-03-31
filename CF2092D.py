def gao(s,lx,ix,tx):
    ret = []
    flag = True
    m = len(s)
    while flag and len(ret)<2*m and (lx>0 or ix >0  or tx >0):
        n = len(s)
        s = list(s)
        ss = []
        add = 0
        for i in range(n-1):
            ss.append(s[i])
            if s[i]!=s[i+1]:
                if s[i]+s[i+1] in ('LI','IL') and tx > 0:
                    tx -= 1
                    ret.append(i+add)
                    add += 1
                    ss.append('T')
                elif s[i]+s[i+1] in ('LT','TL') and ix > 0:
                    ix -= 1
                    ret.append(i+add)
                    add += 1
                    ss.append('I')
                elif s[i]+s[i+1] in ('IT','TI') and lx > 0:
                    lx -= 1
                    ret.append(i+add)
                    add += 1
                    ss.append('L')
        ss.append(s[n-1])
        # print(ss)
        flag = len(ss)>n
        s = ss
    if lx ==0 and ix == 0 and tx == 0:
        return ret
    else:
        return -1
    

def solve():
    n = int(input())
    s = input()
    lm,im,tm = 0,0,0
    for t in s:
        if t == 'L':
            lm+=1
        elif t=='I':
            im+=1
        elif t=='T':
            tm+=1
    if lm == im and im == tm:
        print(0)
    elif lm ==n or im == n or tm == n:
        print(-1)
    else:
        t = max([lm,im,tm])
        i = 0
        k = 3*t - n
        ret = -1
        while k+3*i<=2*n:
            ret = gao(s,t-lm+i,t-im+i,t-tm+i)
            if ret == -1:
                i+=1
            else:
                break
        if ret == -1:
            print(ret)
        else:
            print(len(ret))
            for t in ret:
                print(t+1)

for i in range(int(input())):
    solve()