import sys
n = int(sys.stdin.readline())
arr = [0,1,3]

if n<3:
    print(arr[n]%10007)
else:
    for i in range(3,n+1):
        arr.append(arr[i-2]*2+arr[i-1])
    print(arr[n]%10007)