while True:
    num = int(input())
    cnt = 0
    if num == 0: break
    arr = [True] * ((num*2)+1)
    arr[1] = False
    k = int((2*num)**0.5)+1
    for i in range(2,k+1):
        if arr[i] == True:
            for j in range(i*2, num*2+1, i):
                arr[j] = False
    for i in range(num+1,(num*2)+1):
        if arr[i] == True: cnt +=1
    print(cnt)