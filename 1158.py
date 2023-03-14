import sys
from collections import deque

n,k = map(int, sys.stdin.readline().split())
arr = deque(list(i for i in range(1,n+1)))
ans = deque()
a = k-1
while arr:
    front = arr.popleft()
    a -=1
    if a<0:
        ans.append(front)
        a= k-1
    else:
        arr.append(front)

print("<", end="")
for i in range(len(ans)-1):
  print(ans[i], end=", ")
print(str(ans[len(ans)-1])+">")