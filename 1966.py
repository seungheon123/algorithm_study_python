import sys
from collections import deque

n = int(sys.stdin.readline())

for num in range(n):
    a,b = map(int,sys.stdin.readline().split())
    arr = deque(list(map(int,sys.stdin.readline().split())))
    cnt = 0
    while arr:
        top = max(arr)
        front = arr.popleft()
        b-=1
        if front == top: 
            cnt+=1
            if b<0:
                print(cnt)
                break
        else:
            arr.append(front)
            if b<0:
                b = len(arr)-1
    