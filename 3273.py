num = int(input())
arr = list(map(int,input().split()))
arr.sort()
n = int(input())
cnt = 0
left, right = 0, num-1
while left<right:
    tmp = arr[left] + arr[right]
    if tmp == n: cnt+=1
    elif tmp<n: 
        left+=1
        continue
    right-=1

print(cnt)