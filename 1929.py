a,b = map(int, input().split())
c = int((b**0.5)+1)
arr = [True]*(b+1)
arr[1] = False
for num in range(2,c):
    if arr[num] == True:
        for j in range(num*2, b+1, num):
            arr[j] = False

for i in range(a,b+1):
    if arr[i] == True: print(i)