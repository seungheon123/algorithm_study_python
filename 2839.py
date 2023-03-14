num = int(input())
ans = 0

while num >=0:
    if num % 5 == 0:
        ans += num//5
        print(ans)
        break
    num -=3
    ans +=1
else:
    print(-1)
