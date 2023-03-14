import sys
arr = sys.stdin.readline().strip()
bracket = []
temp = 1
res = 0
for i in range(len(arr)):
    n = arr[i]
    if n =='(':
        temp*=2
        bracket.append(n)
    elif n =='[':
        temp*=3
        bracket.append(n)
    elif n ==')':
        if not bracket or bracket[-1] =='[':
            res = 0
            break
        else:
            if arr[i-1] =='(':
                res+=temp
            temp //=2
            bracket.pop()
    else:
        if not bracket or bracket[-1] =='(':
            res = 0
            break
        else:
            if arr[i-1] =='[':
                res+=temp
            temp //=3
            bracket.pop()

if bracket:
    print(0)
else:
    print(res)