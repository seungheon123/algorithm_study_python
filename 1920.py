n = int(input())
A = sorted(map(int,input().split()))
m = int(input())
K = list(map(int,input().split()))

for i in range(m):
    min = 0
    max = n-1
    while min<=max:
        mid = (min+max)//2
        if K[i] == A[mid]: 
            print(1)
            break
        elif K[i] <A[mid]:
            max = mid-1
        elif K[i] > A[mid]:
            min = mid+1
    else:
        print(0)