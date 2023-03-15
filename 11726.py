import sys
n = int(sys.stdin.readline())

s = [0,1,2]

if n<3:
    print(s[n]%10007)
else:
    for i in range(3,n+1):
        s.append(s[i-1]+s[i-2])
    print(s[n]%10007)
