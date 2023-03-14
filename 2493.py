import sys
n = int(sys.stdin.readline())
top = list(map(int,sys.stdin.readline().split()))

stack = []
ans = [0]*n
for j in range(n-1,-1,-1):
    while stack:
        if top[j] > top[stack[-1]-1]:
            ans[stack[-1]-1] = j+1
            stack.pop()
        else:
            break
    stack.append(j+1)
print(*ans)