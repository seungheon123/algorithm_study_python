import sys
n = int(sys.stdin.readline())
t = []
p = []

dp = [0]*(n+1)

for i in range(n):
    x,y = map(int,sys.stdin.readline().split())
    t.append(x)
    p.append(y)

money = 0
for i in range(n):
    money = max(money,dp[i])
    if i+t[i]>n: continue
    dp[i+t[i]] = max(money+p[i],dp[i+t[i]])

print(max(dp))