import sys

arr = list(input())
stick = []
ans = 0
for i in range(len(arr)):
    if arr[i] == "(":
        stick.append(arr[i])
    else:
        if arr[i-1] == "(":
            stick.pop()
            ans+=len(stick)
        else:
            stick.pop()
            ans+=1
print(ans)