import sys
T = int(sys.stdin.readline())
for _ in range(T):
    P = sys.stdin.readline().strip()
    n = int(sys.stdin.readline())
    que = input()[1:-1].split(',')
    r = 0
    a,b= 0,0
    for i in range(len(P)):
        if P[i] =='R':
            r+=1
        else:
            if r%2==0:
                a+=1
            else:
                b+=1
    if a+b<=n:
        que = que[a:n-b]
        if r%2==0:
            print('['+','.join(que)+']')
        else:
            print('['+','.join(que[::-1])+']')
    else:
        print("error")