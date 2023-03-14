import sys
n,m = map(int,sys.stdin.readline().split())
s = []
cnt = 0
for _ in range(n):
    s.append(sys.stdin.readline())

for _ in range(m):
    str = sys.stdin.readline()
    if str in s:
        cnt+=1

print(cnt)