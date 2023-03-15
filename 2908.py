import sys
x,y = map(int, sys.stdin.readline().split())

x = str(x)
y = str(y)

nx = int(x[2])*100 + int(x[1])*10 + int(x[0])
ny = int(y[2])*100 + int(y[1])*10 + int(y[0])

if nx>ny:
    print(nx)
else:
    print(ny)