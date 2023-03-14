n = int(input())
ans = 0
numbers = map(int, input().split())

for num in numbers:
    cnt = 0
    if num > 1:
        for i in range(2,num+1):
            if num % i == 0:
                cnt+=1
        if cnt == 1:
            ans += 1

print(ans)