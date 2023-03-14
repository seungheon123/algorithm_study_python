import heapq
import sys
n = int(sys.stdin.readline())
left = []
right = []

for _ in range(n):
    x = int(sys.stdin.readline())
    if len(left) == len(right):
        heapq.heappush(left,(-x,x))
        if right:
            if left[0][1]>right[0]:
                temp1 = heapq.heappop(left)[1]
                temp2 = heapq.heappop(right)
                heapq.heappush(left,(-temp2,temp2))
                heapq.heappush(right,temp1)
    else:
        heapq.heappush(right,x)
        if left[0][1] > right[0]:
            temp1 = heapq.heappop(left)[1]
            temp2 = heapq.heappop(right)
            heapq.heappush(left,(-temp2,temp2))
            heapq.heappush(right,(temp1))
    print(left[0][1])