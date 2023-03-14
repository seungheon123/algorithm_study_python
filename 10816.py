import sys

n = int(sys.stdin.readline())
arr = sorted(list(map(int,sys.stdin.readline().split())))
m = int(sys.stdin.readline())
arr_ = list(map(int,sys.stdin.readline().split()))
hash = {}

for i in arr:
    if i in hash:
        hash[i]+=1
    else:
        hash[i] = 1
for i in arr_:
    if i in hash:
        print(hash[i],end=" ")
    else:
        print(0,end=" ")