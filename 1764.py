import sys
n,m = map(int, sys.stdin.readline().split())
neverseen = {}
never = []
cnt = 0
for _ in range(n):
    str = sys.stdin.readline().rstrip()
    neverseen[str] = 1
for _ in range(m):
    str = sys.stdin.readline().rstrip()
    if str in neverseen:
        never.append(str)
        cnt+=1

print(cnt)
never.sort()
for i in range(len(never)):
    print(never[i])