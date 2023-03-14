arr = [False]*2 + [True]*10002
for num in range(2,int(10002**0.5)+1):
    if arr[num] == True:
        for j in range(num*2, 10002, num):
            arr[j] = False


n = int(input())
while n>0:
    num = int(input())
    if num<4:
        continue
    else:
        min = 10000
        ans = 0
        for i in range(1,num):
            if arr[i] and arr[num-i]:
                if min>abs((num-i) - i): 
                    min = abs((num-i)-i)
                    ans = i

        print(ans, num-ans)
    n-=1