import sys
n,m = map(int,sys.stdin.readline().split())
coin = []
dp = [0]*(m+1)
dp[0] = 1
for _ in range(n):
    value = int(sys.stdin.readline())
    coin.append(value)

for i in coin:
    for j in range(i,m+1):
        dp[j] += dp[j-i]

print(dp[m])