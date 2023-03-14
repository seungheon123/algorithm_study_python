n = int(input())
while n>0:
    string = input()
    stack = []
    for i in range(len(string)):
        if string[i] == ')':
            if len(stack) !=0:
                if stack[-1] == '(': 
                    stack.pop()
                    continue
        stack.append(string[i])
    if len(stack) == 0: print("YES")
    else: print("NO")
    n-=1