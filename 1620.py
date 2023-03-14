import sys
table_alpha = {}
table_num = {}
n,m = map(int,sys.stdin.readline().split())
for i in range(1,n+1):
    poke = sys.stdin.readline().rstrip()
    table_alpha[poke] = i
    table_num[i] = poke

for _ in range(m):
    question = sys.stdin.readline().rstrip()
    if question.isalpha():
        print(table_alpha[question])
    else:
        question = int(question)
        print(table_num[question])