n = int(input())
arr = []
sum = 0
while n>0:
    a = int(input())
    if a == 0: 
        sum-=arr.pop()
    else:
        arr.append(a)
        sum+=a
    n-=1
print(sum)