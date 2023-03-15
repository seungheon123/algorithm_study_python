import sys
w = sys.stdin.readline()
arr = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']

time = 0

for i in range(len(w)):
    for j in range(len(arr)):
        if w[i] in arr[j]:
            time +=(j+3)

print(time)
