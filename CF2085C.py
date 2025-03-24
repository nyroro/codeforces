def solve(x,y):
    if (x&y) == 0:
        return 0
    elif x == y:
        return -1
    else:
        if x < y:
            x,y = y,x
        k = 0

        while (x&y) != 0:
            t = x&y
            t1 = x^y

            if (t&-t) <(t1&-t1):
                v = (t&-t)
                x+=v
                y+=v
                k+=v
            elif (t1 & ((t&-t) - 1)) == (t1&-t1):
                v = (t1&-t1)
                if x&v:
                    x+=v
                if y&v:
                    y+=v
                k+=v
            else:
                v = (t1&-t1)
                if x & v:
                    x-=v
                if y&v:
                    y-=v

        return k


for i in range(int(input())):
    x,y = map(int,input().split())
# for x in range(1,100):
#     for y in range(x+1,100):
    val = solve(x,y)
    print(val)
        # if val != -1:
        #     assert ((x+val)&(y+val)) == 0