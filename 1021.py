import sys
from collections import deque
n,m = map(int,sys.stdin.readline().split())
arr = map(int,sys.stdin.readline().split())
arr_ = list(i for i in range(1,n+1))
que = deque(arr)
list =deque(arr_)
cnt= 0
while len(que)>0:
    i = que[0]
    if i == list[0]:
        list.popleft()
        que.popleft()
    else:
        if len(list)//2< list.index(i):
            while True:
                if i == list[0]: break
                a = list[-1]
                list.insert(0,a)
                list.pop()
                cnt+=1
        else:
            while True:
                if i ==list[0]: break
                a = list[0]
                list.append(a)
                list.popleft()
                cnt+=1
print(cnt)