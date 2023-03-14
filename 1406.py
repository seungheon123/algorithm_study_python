import sys
left = list(sys.stdin.readline().strip())
right = []
n = int(sys.stdin.readline())


for _ in range(n):
    command = sys.stdin.readline().split()
    if command[0] == 'L':
        if len(left) !=0:
            right.append(left[-1])
            left.pop()
    elif command[0] == 'D':
        if len(right) !=0:
            left.append(right[-1])
            right.pop()
    elif command[0] =='B':
        if len(left) !=0:
            left.pop()
    elif command[0] == 'P':
        left.append(command[1])

while len(left)>0:
    right.append(left[-1])
    left.pop()

while len(right)>0:
    print(right[-1],end="")
    right.pop()

